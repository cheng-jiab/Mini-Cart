from django.db import models
from category.models import Category
from django.urls import reverse

VARIATION_CATEGORY_CHOICE=  (
        ('Color', 'Color'),
        ('Size', 'Size'),
        ('Storage', 'Storage'),
        ('Memory', 'Memory'),
        ('Material', 'Material'),
        ('Speed', 'Speed'),
 
    )

# Create your models here.
class Product(models.Model):
    productName     = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.CharField(max_length=500, blank=True)
    price           = models.DecimalField(max_digits=8, decimal_places=2)
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    isAvailable     = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdDate     = models.DateTimeField(auto_now_add=True)
    modifiedDate    = models.DateTimeField(auto_now=True)
    variationCategory = models.CharField(max_length=100, choices=VARIATION_CATEGORY_CHOICE)

    def getUrl(self):
        return reverse('productDetail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.productName
'''
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variationCategory='color', isActive=True)

    def sizes(self):
        return super(VariationManager, self).filter(variationCategory='size', isActive=True)
'''

class Variation(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variationCategory = models.CharField(max_length=100, choices=VARIATION_CATEGORY_CHOICE)
    variationValue = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    #objects = VariationManager()
    def __str__(self):
        return self.variationValue


