from django.contrib import admin
from .models import Category

# Register your models here. 
class CategoryAdmin(admin.ModelAdmin):
    #prepopulate slug field. Referene: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields
    prepopulated_fields = {'slug': ('categoryName',)}
    list_display = ('categoryName', 'slug')


admin.site.register(Category, CategoryAdmin)
