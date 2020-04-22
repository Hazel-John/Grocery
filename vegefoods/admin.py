from django.contrib import admin
from .models import Items, OrderItem, Order

# Register your models here.
admin.site.register(Items)
admin.site.register(OrderItem)
admin.site.register(Order)

