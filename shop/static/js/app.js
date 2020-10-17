// Checkout page

if (localStorage.getItem('cart') == null) {
    var cart = {}
}
else { cart = JSON.parse(localStorage.getItem('cart')) }

console.log(cart)
if ($.isEmptyObject(cart)) {
    $('#item').append(`<li class="list-group-item d-flex justify-content-between align-items-center">
Your cart is empty please add some item to checckout
</li>`)
}
else {
    var totalitem = 0
    var totalprice = 0;
    var sum = 0;
    for (var item in cart) {
        let name = cart[item][1];
        let qty = cart[item][0];
        let itemPrice = cart[item][2];
        totalprice = totalprice + qty * itemPrice
        totalitem += qty
        sum += qty;
        mystr = `<li class="list-group-item d-flex justify-content-between align-items-center">
    ${name}
    <span class="badge badge-primary badge-pill">${qty}</span></li>`
        $('#item').append(mystr)
    }
    $('#item').append(`<li class="list-group-item d-flex justify-content-between align-items-center">
<h6>Total items</h6>
<span class="badge badge-primary badge-pill">${totalitem}</span></li>
<li class="list-group-item bg-secondary text-white d-flex justify-content-between align-items-center">
<h4>Your cart total price is </h4>
<b><h4 id='totalprice'>${totalprice}</h4>Rs</b></li>`);
$('#amount').val(parseInt($('#totalprice').html()));


}
document.getElementById('cart').innerHTML = sum;

// Sending cart items to database
$('#itemjson').val(JSON.stringify(cart));






// Find out the items in thet cart
if (localStorage.getItem('cart') == null) {
    var cart = {};

} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart)
    updatePopover(cart)


}


// if the add to cart button is clicked, add/increment the button
// $('.cart').click(function () {
$('.divpr').on('click', 'button.cart', function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;
        name = document.getElementById('name' + idstr).innerHTML;
        price = document.getElementById('price' + idstr).innerHTML;
        console.log(price)
        cart[idstr] = [qty, name, parseInt(price)];
        console.log(cart)
    }
    else {
        qty = 1;
        console.log(idstr)
        name = document.getElementById('name' + idstr).innerHTML;
        price = document.getElementById('price' + idstr).innerHTML;
        console.log(price)
        cart[idstr] = [qty, name, parseInt(price)];
    }
    updateCart(cart)
})
updatePopover(cart)

// Add popover to the cart 
$('#popcart').popover()


function updatePopover(cart) {
    var popStr = "";
    var i = 1
    popStr = popStr + "<h5>Your items in cart</h5><div class='m-2'> ";
    for (var item in cart) {
        popStr = popStr + "<b>" + i + " </b>."
        popStr = popStr + document.getElementById('name' + item).innerText.slice(0, 9) + "...Qty : " + cart[item][0] + '<br>'
        i++;
    }
    popStr = popStr + "</div>"
    document.getElementById('popcart').setAttribute('data-content', popStr)
    $('#popcart').popover('toggle')

}

function clearCart() {
    if (confirm("Do You want to remove all the items from the cart")) {
        cart = JSON.parse(localStorage.getItem('cart'))
        for (var item in cart) {
            document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary minus">Add to Cart</button>';
        }
        localStorage.clear();
        cart = {}
        updateCart(cart)
    }
}

// Update cart
function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item][0];
        document.getElementById('div' + item).innerHTML = '<button id="minus' + item + '" class="btn btn-primary minus">-</button><span id="val' + item + '">' + cart[item][0] + '</span><button class="btn btn-primary plus" id="plus' + item + '" >+</button>';
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart)
}

// If plus or minus button is clicked , change the cart value as well as display the value

$('.divpr').on('click', 'button.minus', function () {
    a = this.id.slice(5,)
    cart[a][0] = cart[a][0] - 1
    cart[a][0] = Math.max(0, cart[a][0])
    if (cart[a][0] == 0) {
            document.getElementById('div' + a).innerHTML = '<button id="' + a + '" class="btn btn-primary minus">Add to Cart</button>';
            delete cart[a];
    }
    else {
        document.getElementById('val' + a).innerHTML = cart[a][0]

    }
    updateCart(cart)

})


$('.divpr').on('click', 'button.plus', function () {
    a = this.id.slice(4,)
    cart[a][0] = cart[a][0] + 1
    document.getElementById('val' + a).innerHTML = cart[a][0]
    updateCart(cart)
})



