
from django.contrib import admin
from django.urls import path,include 
#import static files

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('man/',include('man.urls',namespace='man')),
    path('shipp/',include('shipp.urls',namespace='shipp')),
    path('products/',include('products.urls',namespace='products'))
 
    
]# add these lines to serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
