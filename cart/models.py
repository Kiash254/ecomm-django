from django.db import models
from products.models import Products

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    def __str__(self):
        return self.product.name