from django.urls import path
from .views import Homeview

app_name = 'core'
urlpatterns = [
    path('', Homeview, name='home'),
]