from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import NewPostShipping, UkrPostShipping


class NewPostShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPostShipping
        fields = ('id', 'user', 'type_of_delivery', 'city', 'department_address', 'home_address', 'np_post_box')
        extra_kwargs = {
            'user': {'read_only': True},
        }
    
    def validate_np_post_box(self, value):
        if value is not None and value < 1:
            raise serializers.ValidationError("Значення поля 'Поштомат' повинно бути більшим за нуль.")
        return value
       
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        type_of_delivery = validated_data['type_of_delivery']
        
        if type_of_delivery == 'department' and validated_data['department_address'] == '':
            raise APIException(
                detail=f'Поле "Відділення НП" не може бути порожнім.',
                code=400
            )
        elif type_of_delivery == 'address' and validated_data['home_address'] == '':
            raise APIException(
                detail=f'Поле "Адреса" не може бути порожнім.',
                code=400
            )
        elif type_of_delivery == 'np_post_box' and validated_data['np_post_box'] == None:
            raise APIException(
                detail=f'Поле "Поштомат" не може бути порожнім.',
                code=400
            )

            
        new_post_shipping = NewPostShipping.objects.create(user=user, **validated_data)
        
        return new_post_shipping


class UkrPostShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UkrPostShipping
        fields = ('id', 'user', 'city', 'index')
        extra_kwargs = {
            'user': {'read_only': True},
        }
    
    def validate_index(self, value):
        if value is not None and value < 1:
            raise serializers.ValidationError("Значення поля 'Індекс' повинно бути більшим за нуль.")
        return value
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        ukr_post_shipping = UkrPostShipping.objects.create(user=user, **validated_data)
        
        return ukr_post_shipping
