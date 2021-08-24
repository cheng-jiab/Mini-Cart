from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    catImage = models.ImageField(upload_to='photos/categories/', blank=True)

    def getUrl(self):
        return reverse('productsByCategory', args=[self.slug])


    # Change the model names shown in admin page.
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

        

    def __str__(self):
        return self.categoryName
