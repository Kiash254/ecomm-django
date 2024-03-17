from django.urls import path
from .views import Accountview

app_name='accounts'
urlpatterns=[
    path('',Accountview,name='account')
]