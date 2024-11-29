from rest_framework import serializers

from basket import models
from basket.models import Basket, BasketItem


class BasketItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = BasketItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'items']


class BasketSummarySerializer(serializers.ModelSerializer):
    """Сериализатор корзины для подробного отображения"""

    items = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['id', 'user', 'items', 'total_quantity', 'total_price']

    def get_items(self, obj):
        """Получаем список продуктов в корзине"""

        items = BasketItem.objects.filter(basket=obj)
        return [
            {
                'product_id': item.product.id,
                'product_name': item.product.name,
                'price': item.product.price,
                'quantity': item.quantity,
                'total_price': item.quantity * item.product.price
            }
            for item in items
        ]

    def get_total_quantity(self, obj):
        """Общее количество товаров в корзине"""
        return BasketItem.objects.filter(basket=obj).aggregate(total=models.Sum('quantity'))['total'] or 0

    def get_total_price(self, obj):
        """Общая стоимость корзины"""
        return sum(item.quantity * item.product.price for item in BasketItem.objects.filter(basket=obj))
