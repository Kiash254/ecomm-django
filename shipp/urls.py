from django.urls import path
from .views import ShippView

app_name = 'shipp'
urlpatterns=[
    path('',ShippView,name='ship')
]