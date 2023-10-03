from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializer import CreateUserSerializer, UpdateUserSerializer, ChangeUserPasswordSerializer, DestroyUserSerializer


User = get_user_model()


class UserCreateApiView(generics.CreateAPIView):
    """
    API view for creating a new User instance.
    """
    
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserAPIView(generics.RetrieveUpdateAPIView):
    """
    API view to update user profile.
    """
    
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user


class UserListAPIView(generics.ListAPIView):
    """
    API view for retrieving a list of User instances.
    """
    
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class ChangePasswordView(generics.UpdateAPIView):
    """
    API view for changing a user's password.
    """
    serializer_class = ChangeUserPasswordSerializer
    
    def get_object(self):
        return self.request.user
