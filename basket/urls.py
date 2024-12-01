from django.urls import path
from .views import (
    BasketItemCreateAPIView,
    BasketDetailAPIView,
    BasketItemDeleteAPIView,
    BasketClearAPIView, BasketItemUpdateAPIView,
)

urlpatterns = [
    path('add/', BasketItemCreateAPIView.as_view(), name='basket-add'),
    path('update/<int:product_id>/', BasketItemUpdateAPIView.as_view(), name='basket-update'),
    path('detail/', BasketDetailAPIView.as_view(), name='basket-detail'),
    path('delete/<int:pk>/', BasketItemDeleteAPIView.as_view(), name='basket-item-delete'),
    path('clear/', BasketClearAPIView.as_view(), name='basket-clear'),
]
