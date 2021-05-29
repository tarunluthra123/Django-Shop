from rest_framework import serializers

from api import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(read_only=True, source='product')

    class Meta:
        fields = (
            'id', 'user', 'product', 'product_detail', 'delivered', 'createdAt'
        )
        model = models.Order
