from django.urls import path 
from .views import Cartview
app_name = 'cart'
urlpatterns = [
    path('', Cartview, name='cart'),
]