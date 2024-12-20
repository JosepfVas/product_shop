# Generated by Django 5.1.3 on 2024-12-01 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0002_rename_cart_basketitem_basket_and_more"),
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="basketitem",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="basket",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="basket",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="basketitem",
            name="basket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="basket.basket",
                verbose_name="Корзина",
            ),
        ),
        migrations.AlterField(
            model_name="basketitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="basketitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Количество"),
        ),
        migrations.RemoveField(
            model_name="basketitem",
            name="added_at",
        ),
    ]
