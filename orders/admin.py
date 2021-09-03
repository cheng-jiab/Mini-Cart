from django.contrib import admin
from .models import *


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderNumber', 'fullName', 'phone', 'email', 'orderTotal']
    list_per_page = 20
    inlines = [OrderProductInline, ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)