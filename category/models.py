from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/category', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('category_by_product', args=[self.slug])
