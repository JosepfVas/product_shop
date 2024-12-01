from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    """Модель корзины, связанная с пользователем"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="basket",
        verbose_name="Пользователь",
    )

    def get_total_price(self):
        """Подсчет общей стоимости товаров в корзине"""
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        """Подсчет общего количества товаров"""
        return sum(item.quantity for item in self.items.all())


class BasketItem(models.Model):
    """Модель элемента корзины"""

    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name="items", verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def get_total_price(self):
        """Подсчет стоимости текущего товара"""
        return self.product.price * self.quantity
