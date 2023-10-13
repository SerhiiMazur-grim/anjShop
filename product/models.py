import os
import shutil

from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='products_created', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name='products_updated', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        folder_path = os.path.join(settings.MEDIA_ROOT, self.sku)

        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        super(Product, self).delete(*args, **kwargs)
    

def product_image_upload_to(instance, filename):
    return f'{slugify(instance.product.sku)}/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_upload_to, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.product} image: {self.image}'
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(ProductImage, self).delete(*args, **kwargs)
