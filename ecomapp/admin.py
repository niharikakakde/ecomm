from django.contrib import admin
from .models import Product,cart,orders


# Register your models here.
class ProdAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','cat','is_active']
    list_filter=['cat','is_active']
class cartAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','order_id','uid','pid']


admin.site.register(cart,cartAdmin)
admin.site.register(Product,ProdAdmin)
admin.site.register(orders,OrderAdmin)