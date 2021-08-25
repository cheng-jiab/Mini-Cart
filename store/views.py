from category.models import Category
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cartId

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


def productDetail(request, categorySlug=None, productSlug=None):
    try:
        #  "__" : to query using the attributes of the many-to-many-related model:
        singleProduct = Product.objects.get(category__slug=categorySlug, slug=productSlug)
        inCart = CartItem.objects.filter(cart__cartId=_cartId(request), product=singleProduct).exists()  
        
    except Exception as e:
        raise e

    context = {
        'singleProduct' : singleProduct,
        'inCart': inCart,
    }
    return render(request, 'store/productDetail.html', context)