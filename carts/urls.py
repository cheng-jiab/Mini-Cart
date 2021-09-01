from django.urls import path
from django.urls import path
from . import views

urlpatterns= [
    path('', views.cart, name='cart'),
    path('addCart/<int:productId>', views.addCart, name='addCart'),
    path('decreaseCartItem/<int:cartItemId>', views.decreaseCartItem, name='decreaseCartItem'),
    path('removeItem/<int:cartItemId>', views.removeItem, name='removeItem'),
    path('increaseCartItem/<int:cartItemId>', views.increaseCartItem, name='increaseCartItem'),
    path('checkout/', views.checkout, name='checkout'),
]
