from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('placeOrder/', views.placeOrder, name='placeOrder'),
    path('payments/', views.payments, name='payments'),
    path('orderComplete/<int:orderId>', views.orderComplete, name='orderComplete')
]