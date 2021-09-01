from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product, Variation
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
# How to use session: Ref https://docs.djangoproject.com/en/3.2/topics/http/sessions/#using-sessions-out-of-views
def _cartId(request):
    cartId = request.session.session_key
    if not cartId:
        cartId = request.session.create()
    return cartId


def addCart(request, productId):
    product = Product.objects.get(id=productId)
    
    #productVariation = []
    if request.method == 'POST':
        for item in request.POST:
            value = request.POST[item]
            try:
                variation = Variation.objects.get(product=product, variationCategory__iexact=item, variationValue__iexact=value)
                
            except:
                pass
   
    try:
        cart = Cart.objects.get(cartId=_cartId(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cartId = _cartId(request)
        )
        cart.save()
    
    try:
        cartItem = CartItem.objects.get(product=product, cart=cart, variation=variation) 
        cartItem.quantity += 1
        
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            variation=variation
            
        )
    '''    
    if len(productVariation) > 0:
        for item in productVariation:
            cartItem.variations.add(item)

    '''
    cartItem.save()
    return redirect('cart')

def increaseCartItem(request, cartItemId):
    cartItem = CartItem.objects.get(id=cartItemId)
    cartItem.quantity += 1
    cartItem.save()
    return redirect('cart')

def decreaseCartItem(request, cartItemId):
    cartItem = CartItem.objects.get(id=cartItemId)
    if cartItem.quantity > 1:
        cartItem.quantity -= 1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('cart')

def removeItem(request, cartItemId):
    cartItem = CartItem.objects.get(id=cartItemId)
    cartItem.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cartItems=None):
    try:
        cart = Cart.objects.get(cartId=_cartId(request))
        cartItems = CartItem.objects.filter(cart=cart, isActive=True)
        for cartItem in cartItems:
            total += (cartItem.product.price * cartItem.quantity)
            quantity += cartItem.quantity
        tax = round((0.07*total),2)
        totalAfterTax = total + tax
    except ObjectDoesNotExist:
        pass
        
    context = {
        'total': total,
        'quantity': quantity,
        'cartItems': cartItems,
        'tax': tax,
        'totalAfterTax': totalAfterTax
    }
    return render(request, 'store/cart.html', context)
    
@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cartItems=None):
    try:
        cart = Cart.objects.get(cartId=_cartId(request))
        cartItems = CartItem.objects.filter(cart=cart, isActive=True)
        for cartItem in cartItems:
            total += (cartItem.product.price * cartItem.quantity)
            quantity += cartItem.quantity
        tax = round((0.07*total),2)
        totalAfterTax = total + tax
    except ObjectDoesNotExist:
        pass
        
    context = {
        'total': total,
        'quantity': quantity,
        'cartItems': cartItems,
        'tax': tax,
        'totalAfterTax': totalAfterTax
    }
    return render(request, 'store/checkout.html', context)
