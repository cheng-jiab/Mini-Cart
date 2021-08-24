from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    productName     = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.CharField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    isAvailable     = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdDate     = models.DateTimeField(auto_now_add=True)
    modifiedDate    = models.DateTimeField(auto_now=True)

    def getUrl(self):
        return reverse('productDetail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.productName
        