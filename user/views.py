from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializer import CreateUserSerializer, UpdateUserSerializer, ChangeUserPasswordSerializer


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


class UserDeleteView(generics.DestroyAPIView):
    """
    API view for delet User instance.
    """
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        # Перевірка введеного пароля
        password = request.data.get('password')
        if not password:
            return Response({'detail': 'Поле пароля обов\'язкове'}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, instance.password):
            return Response({'detail': 'Неправильний пароль'}, status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'detail': 'Користувач видалений'}, status=status.HTTP_204_NO_CONTENT)
