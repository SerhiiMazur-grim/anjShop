from django.urls import path

from . import views


urlpatterns = [
    path('api/product/create/', views.ProductCreateView.as_view(), name='create_product'),
    path('api/product/<int:pk>/', views.ProductDetailView.as_view(), name='detail_product'),
    path('api/product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
]

