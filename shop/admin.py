from django.contrib import admin
from . models import Product, Contact,Orders , OrderUpdate
from django.contrib.admin import AdminSite,ModelAdmin
# Register your models here.

admin.site.site_header="KRishna"
admin.site.register(Product)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
    # search_fields = ('product_name','category','subcategory')
    # list_display= ("category",'product_name')
    # list_filter = ('pub_date',)


admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
