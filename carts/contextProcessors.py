# ref: https://docs.djangoproject.com/en/3.2/ref/templates/api/#writing-your-own-context-processors

from .models import Cart, CartItem
from .views import _cartId

def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        cartCount = 0
        try:
            cart = Cart.objects.filter(cartId=_cartId(request))
            cartItems = CartItem.objects.all().filter(cart=cart[:1])
            for cartItem in cartItems:
                cartCount = cartCount + cartItem.quantity
        except Cart.DoesNotExist:
            pass
    return dict(cartCount=cartCount)