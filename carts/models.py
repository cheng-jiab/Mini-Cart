from django.db import models
from store.models import Product, Variation
from accounts.models import Account 

# Create your models here.

class Cart(models.Model):
    cartId      = models.CharField(max_length=250, blank=True)
    dateAdded   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cartId


class CartItem(models.Model):
    #allow logged user to see previous cart itmes
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations  = models.ManyToManyField(Variation, blank=True)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity    = models.IntegerField()
    isActive    = models.BooleanField(default=True)

    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.productName