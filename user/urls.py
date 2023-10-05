from django.urls import path

from . import views


urlpatterns = [
    path('api/user/list/', views.UserListAPIView.as_view(), name='users_list'),
    path('api/user/register/', views.UserCreateApiView.as_view(), name='create_user'),
    path('api/user/update/', views.UpdateUserAPIView.as_view(), name='update_user'),
    path('api/user/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('api/user/delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user')
]

