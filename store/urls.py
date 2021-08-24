
from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:categorySlug>", views.store, name="productsByCategory")
]