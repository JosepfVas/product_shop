from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from basket.models import Basket, BasketItem
from basket.serializers import BasketItemSerializer, BasketSerializer
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotFound


class BasketItemCreateAPIView(generics.CreateAPIView):
    """Добавление товара в корзину"""
    serializer_class = BasketItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        basket, created = Basket.objects.get_or_create(user=self.request.user)
        product = serializer.validated_data['product_id']

        # Проверка, есть ли уже этот продукт в корзине
        if BasketItem.objects.filter(basket=basket, product=product).exists():
            raise ValidationError({"detail": "Этот продукт уже есть в корзине. Используйте обновление количества."})

        # Создание нового элемента корзины
        serializer.save(basket=basket)


class BasketItemUpdateAPIView(generics.UpdateAPIView):
    """Обновление количества товара в корзине"""
    serializer_class = BasketItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'product_id'

    def get_object(self):
        """Получает элемент корзины по продукту и пользователю"""
        # Проверяем наличие корзины у пользователя
        try:
            basket = self.request.user.basket
        except Basket.DoesNotExist:
            raise NotFound({"detail": "Корзина пользователя не найдена."})

        # Получаем ID продукта из URL
        product_id = self.kwargs.get(self.lookup_field)

        # Пытаемся найти элемент корзины
        try:
            return BasketItem.objects.get(basket=basket, product_id=product_id)
        except BasketItem.DoesNotExist:
            raise NotFound({"detail": "Элемент корзины не найден для указанного продукта."})

    def perform_update(self, serializer):
        """Обновляет количество товара"""
        basket_item = self.get_object()  # Убедимся, что объект существует
        quantity = serializer.validated_data.get('quantity', 1)

        # Обновление количества
        basket_item.quantity = quantity
        basket_item.save()


class BasketDetailAPIView(generics.RetrieveAPIView):
    """Просмотр содержимого корзины"""
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        basket, created = Basket.objects.get_or_create(user=self.request.user)
        return basket


class BasketItemDeleteAPIView(generics.DestroyAPIView):
    """Удаление товара из корзины"""
    serializer_class = BasketItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BasketItem.objects.filter(basket__user=self.request.user)


class BasketClearAPIView(APIView):
    """Полная очистка корзины"""
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.items.all().delete()
        return Response({"detail": "Корзина очищена"}, status=status.HTTP_204_NO_CONTENT)
