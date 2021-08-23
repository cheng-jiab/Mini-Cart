from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =('productName', 'price', 'stock', 'category', 'modifiedDate', 'isAvailable')
    prepopulated_fields = {'slug' : ('productName',)}

admin.site.register(Product, ProductAdmin)