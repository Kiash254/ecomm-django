from django.contrib import admin
from .models import Order
from .models import CustomUser
admin.site.register(Order)
admin.site.register(CustomUser)

