from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')
        extra_kwargs = {
            'cart': {'read_only': True},
        }
        
    def create(self, validated_data):
        request = self.context.get('request')
        product = validated_data['product']
        quantity = int(validated_data['quantity'])

        if product.quantity < quantity:
            raise APIException(
                detail=f'Недостатньо товару на складі. Кількість товару на складі: {product.quantity}',
                code=400
            )

        if quantity < 1:
            quantity = 1
            
        cart = request.user.user_cart.get()
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        
        return cart_item

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity', instance.quantity)
        if quantity < 1:
            quantity = 1

        product = instance.product
        if product.quantity < quantity:
            quantity = product.quantity

        instance.quantity = quantity
        instance.save()

        return instance
