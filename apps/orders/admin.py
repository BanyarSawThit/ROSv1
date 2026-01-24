from django.contrib import admin
from apps.orders.models import Order, OrderItem

# Register your models here.
admin.site.register((Order, OrderItem))