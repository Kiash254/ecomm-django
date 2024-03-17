from django.db import models

# Create your models here.
class Shipping(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name