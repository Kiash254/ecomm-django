from django.shortcuts import render

# Create your views here.
def Cartview(request):
    return render(request,'cart.html')