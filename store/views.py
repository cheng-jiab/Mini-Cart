from django.http.response import HttpResponse
from category.models import Category
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cartId
# ref: https://docs.djangoproject.com/en/3.2/topics/pagination/
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

def store(request, categorySlug=None):
    categories = None
    products = None

    if categorySlug != None:
        categories = get_object_or_404(Category, slug=categorySlug)
        products = Product.objects.filter(category=categories, isAvailable=True)
        productCount = products.count()
    else:
        products = Product.objects.all().filter(isAvailable=True).order_by('id')
        productCount = products.count()
    
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    pagedProducts = paginator.get_page(page)

    context = {
        'products' : pagedProducts,
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

def search(request):
    # Search use objects.filter() function. Ref: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#icontains
    products = None
    productCount = 0
    if 'keyword' in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            # Logical OR in filter function using Q() Ref: https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects
            products = Product.objects.order_by('-createdDate').filter(Q(description__icontains=keyword) | Q(productName__icontains=keyword))
            productCount = products.count()
    context = {
        'products': products,
        'productCount': productCount
    }
    return render(request, 'store/store.html', context)