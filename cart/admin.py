from django.contrib import admin
from cart.models import Products , Contact , Order , OrderUpdate

# Register your models here.

admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
