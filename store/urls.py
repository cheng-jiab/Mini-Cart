
from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:categorySlug>", views.store, name="productsByCategory"),
    path("<slug:categorySlug>/<slug:productSlug>", views.productDetail, name="productDetail"),
]

#Reference: https://docs.djangoproject.com/en/3.2/topics/http/urls/