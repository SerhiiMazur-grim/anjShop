from django.urls import path

from . import views


urlpatterns = [
    path('api/cart_item/create/', views.CartItemCreateView.as_view())
]