from django.contrib import admin
from .models import Product, Variation


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =('productName', 'price', 'stock', 'category', 'modifiedDate', 'isAvailable')
    prepopulated_fields = {'slug' : ('productName',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variationCategory', 'variationValue', 'isActive')
    list_editable = ('isActive', )
    list_filter = ('product', 'variationCategory', 'variationValue')
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)