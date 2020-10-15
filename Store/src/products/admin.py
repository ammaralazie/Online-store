from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternntive)
admin.site.register(Product_Aessories)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAderess)

# Register your models here.
