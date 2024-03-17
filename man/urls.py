from django.urls import path
from .views import ManufacturerView

app_name ='man'
urlpatterns = [
    path('', ManufacturerView, name='manufacturer'),
]

