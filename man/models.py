from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    description= models.TextField()
    def __str__(self):
        return self.name