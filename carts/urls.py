from django.urls import path
from django.urls import path
from . import views

urlpatterns= [
    path('', views.cart, name='cart'),
    path('addCart/<int:productId>', views.addCart, name='addCart'),
    path('removeCart/<int:productId>', views.removeCart, name='removeCart'),
    path('removeItem/<int:productId>', views.removeItem, name='removeItem'),
    path('checkout/', views.checkout, name='checkout'),
]