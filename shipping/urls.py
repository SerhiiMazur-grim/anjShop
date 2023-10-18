from django.urls import path

from . import views


urlpatterns = [
    path('api/shipping/np/create/', views.NewPostShippingCreateView.as_view()),
    path('api/shipping/ukr/create/', views.UkrPostShippingCreateView.as_view()),
    # path('api/cart_item/create/', views.CartItemCreateView.as_view()),
    # path('api/cart_item/create/', views.CartItemCreateView.as_view()),
]