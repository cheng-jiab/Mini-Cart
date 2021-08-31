from django.db import models
from store.models import Product, Variation

# Create your models here.

class Cart(models.Model):
    cartId      = models.CharField(max_length=250, blank=True)
    dateAdded   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cartId


class CartItem(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations  = models.ManyToManyField(Variation, blank=True)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    isActive    = models.BooleanField(default=True)

    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.productName