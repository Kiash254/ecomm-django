from django.db import models
#import user
from django.contrib.auth.models import User
from products.models import Products
from cart.models import Cart
from shipp.models import Shipping

# Create your models here.
#crete a custom user model
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name