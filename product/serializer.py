from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Category, Product, ProductImage


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    
    class Meta:
        model = Product
        fields = ('__all__')

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        
        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') else None
        validated_data['created_by'] = user
        product = Product.objects.create(**validated_data)

        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)

        return product
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') else None
        validated_data['updated_by'] = user
        
        model_fields = [field.name for field in Product._meta.fields]
        for field in model_fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
        
        updated_images_data = validated_data.get('images')
        if updated_images_data:
        
            for image_data in updated_images_data:
                ProductImage.objects.update_or_create(product=instance, image=image_data)
        
        instance.save()
        
        return instance
