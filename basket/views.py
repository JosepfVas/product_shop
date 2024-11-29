from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from basket.serializers import BasketSerializer, BasketItemSerializer, BasketSummarySerializer
from basket.models import Basket, BasketItem


class BasketItemCreateAPIView(generics.CreateAPIView):
    """Добавление товара в корзину"""
    serializer_class = BasketItemSerializer

    def perform_create(self, serializer):
        """Добавление товара в корзину или увеличение его количества"""
        basket = self.request.user.basket
        product = serializer.validated_data['product']

        basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not created:
            basket_item.quantity += serializer.validated_data.get('quantity', 1)
            basket_item.save()
        else:
            serializer.save(basket=basket)


class BasketUpdateAPIView(generics.UpdateAPIView):
    """Обновление количества товара в корзине"""
    serializer_class = BasketItemSerializer

    def get_queryset(self):
        """Обновление товара в корзине текущего пользователя"""
        return BasketItem.objects.filter(basket__user=self.request.user)


class BasketListAPIView(generics.ListAPIView):
    serializer_class = BasketItemSerializer

    def get_queryset(self):
        return BasketItem.objects.filter(basket__user=self.request.user)


class BasketDetailAPIView(generics.RetrieveAPIView):
    """Вывод состава корзины с подсчетом количества и стоимости товаров"""
    serializer_class = BasketSummarySerializer

    def get_object(self):
        """Возвращает корзину текущего пользователя"""
        basket, created = Basket.objects.get_or_create(user=self.request.user)
        return basket


class BasketDeleteAPIView(generics.DestroyAPIView):
    """Удаление товара из корзины"""
    serializer_class = BasketItemSerializer

    def get_queryset(self):
        """Удаление товара из корзины текущего пользователя"""
        return BasketItem.objects.filter(basket__user=self.request.user)


class BasketClearAPIView(APIView):
    """Очистка корзины текущего пользователя"""

    def delete(self, request, *args, **kwargs):
        """Удаляет все товары из корзины текущего пользователя"""
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.items.all().delete()
        return Response({'message': 'Корзина успешно очищена.'}, status=status.HTTP_200_OK)
