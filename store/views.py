from category.models import Category
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

# Create your views here.

def store(request, categorySlug=None):
    categories = None
    products = None

    if categorySlug != None:
        categories = get_object_or_404(Category, slug=categorySlug)
        products = Product.objects.filter(category=categories, isAvailable=True)
        productCount = products.count()
    else:
        products = Product.objects.all().filter(isAvailable=True)
        productCount = products.count()
    
    context = {
        'products' : products,
        'productCount' : productCount,

    }
    
    return render(request,'store/store.html', context)
