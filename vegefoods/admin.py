from django.contrib import admin
from .models import Items, OrderItem, Order,BillingInfo

# Register your models here.
admin.site.register(Items)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingInfo)

