from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('user.urls')),
    path('', include('product.urls')),
    path('', include('cart.urls')),
    path('', include('shipping.urls')),
    
]
