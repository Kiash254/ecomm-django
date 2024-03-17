from django.shortcuts import render

# Create your views here.
def ManufacturerView(request):
    return render(request,'manufacturer.html')