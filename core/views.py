from django.shortcuts import render
from products.models import Products
from shipp.models import Shipping  
from cart.models import Cart
from accounts.models import CustomUser
from man.models import Manufacturer

# Create your views here.
def Homeview(request):
    products = Products.objects.all()[:10]
    shipping= Shipping.objects.all()
    cart = Cart.objects.all()
    user = CustomUser.objects.all()
    manufacturer = Manufacturer.objects.all()
    context = {
                'products':products, 
               'shipping':shipping, 
               'cart':cart,
               'user':user,
               'manufacturer':manufacturer}
    
    
    return render(request,'home.html',context)