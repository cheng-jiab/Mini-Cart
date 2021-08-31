
from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("category/<slug:categorySlug>", views.store, name="productsByCategory"),
    path("category/<slug:categorySlug>/<slug:productSlug>", views.productDetail, name="productDetail"),
    path('search/', views.search, name='search')
]

#Reference: https://docs.djangoproject.com/en/3.2/topics/http/urls/