from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    """ Модель корзины """

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BasketItem(models.Model):
    """ Промежуточная модель для корзины """

    cart = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='связь с корзиной')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='связь с продуктами')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='время добавления')

    class Meta:
        unique_together = ('cart', 'product')  # Один продукт в корзине только один раз
