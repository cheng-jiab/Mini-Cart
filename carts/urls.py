from django.urls import path
from django.urls import path
from . import views

urlpatterns= [
    path('', views.cart, name='cart'),
    path('addCart/<int:productId>', views.addCart, name='addCart')
]