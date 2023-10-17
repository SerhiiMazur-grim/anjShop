from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    products = models.ManyToManyField(Product, through='CartItem')
    
    def __str__(self):
        return f'Cart: {self.user}'
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'Cartitem: {self.cart.user}'
