from django.db import models
import datetime

# Create your models here.

class Product(models.Model):
    product_id  = models.AutoField
    product_name = models.CharField(max_length=200,default = '')
    category = models.CharField(max_length=100,default = '')
    subcategory = models.CharField(max_length=100,default = '')
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=10000,default = '')
    pub_date = models.DateField()
    image = models.ImageField("shop/images" , default = '')


    def __str__(self):
        return self.product_name


class Contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)    
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    desc = models.CharField(max_length=1000)
    reply = models.CharField(max_length=10 , default="No Reply")
    submit_date = models.DateTimeField(max_length=20,default=datetime.datetime.now())

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name= models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=100 ,default='')
    address = models.CharField(max_length=200,default='')
    address2= models.CharField(max_length=200 ,default='')
    phone = models.IntegerField()
    state = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    zipcode = models.IntegerField()
    orderdt = models.DateTimeField(default=datetime.datetime.now())
    orderstatus = models.CharField(max_length=50 , default='pending')

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id =models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] +'...'