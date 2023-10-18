from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class NewPostShipping(models.Model):
    CHOICES = (
        ('department', 'Доставка у відділення "Нової Пошти"'),
        ('address', 'Доставка за адресою'),
        ('np_post_box', 'Доставка у поштомат "Нової Пошти"'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='np_shipping')
    type_of_delivery = models.CharField(max_length=50, choices=CHOICES, default='department')
    city = models.CharField(max_length=150)
    department_address = models.TextField(blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    np_post_box = models.PositiveBigIntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'NewPost shipping for: {self.user}'
    

class UkrPostShipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ukr_shipping')
    city = models.CharField(max_length=150)
    index = models.PositiveBigIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UkrPost shipping for: {self.user}'
