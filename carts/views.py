from django.http.response import HttpResponse

from django.shortcuts import redirect, render
from store.models import Product
from .models import Cart, CartItem

# Create your views here.
# How to use session: Ref https://docs.djangoproject.com/en/3.2/topics/http/sessions/#using-sessions-out-of-views
def _cartId(request):
    cartId = request.session.session_key
    if not cartId:
        cartId = request.session.create()
    return cartId


def addCart(request, productId):
    product = Product.objects.get(id=productId)
    try:
        cart = Cart.objects.get(cartId=_cartId(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cartId = _cartId(request)
        )
        cart.save()

    try:
        cartItem = CartItem.objects.get(product=product, cart=cart)
        cartItem.quantity += 1
        cartItem.save()
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cartItem.save()
        
    return HttpResponse(cartItem.quantity)
    return redirect('cart')

def cart(request):
    return render(request, 'store/cart.html')
    
