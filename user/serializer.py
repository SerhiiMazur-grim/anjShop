from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model


User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'receive_newsletter')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'receive_newsletter')
    
    def update(self, instance, validated_data):
        user = User.objects.update_user(instance, **validated_data)
        return user


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    
    current_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', 'current_password', 'new_password')
        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
        }
        
    def validate_current_password(self, value):
        user = self.context['request'].user

        if not check_password(value, user.password):
            raise serializers.ValidationError(_('Current password is incorrect.'))

        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        
        return instance
