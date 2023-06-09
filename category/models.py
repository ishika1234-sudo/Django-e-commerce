from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, unique=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True) # the path where all images will be stored on upload
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('product', args=[self.slug])

    # string representation of the model
    def __str__(self) -> str:
        return self.category_name