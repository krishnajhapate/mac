from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from paytm import Checksum
MERCHANT_KEY='YjCep_e3heca4SWi'
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    allProds = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds}
    return render(request, "shop/index.html", params)

def searchMatch(query,item):
    """returns true only if query matches the item"""
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    else:
        return False


def search(request):
    query= request.GET.get('search')
    print(query)
    allProds = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query.lower(),item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prodtemp)!=0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds,'msg':'','query':query}
    if len(allProds)==0 or len(query)<3:
        params={'msg':"Please make sure your search is relevant"}
    return render(request, "shop/search.html", params)




def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        param = True
        print(name, email, phone, desc)
    else:
        param = False

    return render(request, "shop/contact.html", {"param": param})


def view(request, myid):
    product = Product.objects.filter(id=myid).first()

    return render(request, "shop/view.html", {"product": product})


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get("orderid")
        email = request.POST.get("email")
        # return HttpResponse(f"{orderid},{email}")
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({"text": item.update_desc, "time": item.timestamp})
                    response = json.dumps({"status":"success","updates":updates,"itemJson": order[0].items_json}, default=str)
                return HttpResponse(response)

            else:
                return HttpResponse({"status":"noitem"})
        except Exception as e:
            return HttpResponse({"status":"error"})

    return render(request, "shop/tracker.html")




def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        itemjson = request.POST.get("itemjson")
        print(amount)
        order = Orders(
            items_json=itemjson,
            name=name,
            phone=phone,
            email=email,
            address=address,
            address2=address2,
            city=city,
            state=state,
            zipcode=zip,
            amount=amount,
        )
        order.save()
        update = OrderUpdate(
            order_id=order.order_id, update_desc="The Order has been Placed"
        )
        update.save()
        thank = True
        id = order.order_id
        # return render(request, "shop/checkout.html", {"thank": thank, "id": id})

        param_dict = {
            "MID": "UgHuyf92866898213479",
            "ORDER_ID": str(order.order_id),
            "TXN_AMOUNT": str(amount),
            "CUST_ID": email,
            "INDUSTRY_TYPE_ID": "Retail",
            "WEBSITE": "WEBSTAGING",
            "CHANNEL_ID": "WEB",
            "CALLBACK_URL": "http://127.0.0.1:8000/shop/handlerequest/",
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request, "shop/paytm.html", {"param_dict": param_dict})

    return render(request, "shop/checkout.html")


@csrf_exempt
def handlerequest(request):

    form = request.POST
    response_dict = {}
    for i in form:
        response_dict[i] = form[i]
        if i =='CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print("Order was successful")
        else:
            print("Order was unsuccessful")
    return render(request,'shop/paymentstatus.html',{'response':response_dict})
    #  paytm will send you request here
    pass
