from django.db import models
from django.utils.text import slugify

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """Класс категорий"""

    name = models.CharField(max_length=200, verbose_name="название категории")
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="categories/", **NULLABLE, verbose_name="изображение"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def save(self, *args, **kwargs):
        """Генерирует slug на основе имени"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    """Класс подкатегорий"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="ссылка на категорию"
    )
    name = models.CharField(max_length=200, verbose_name="название подкатегории")
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="subcategories/", **NULLABLE, verbose_name="изображение"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def save(self, *args, **kwargs):
        """Генерирует slug на основе имени"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Класс продуктов"""

    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, verbose_name="ссылка на подкатегорию"
    )
    name = models.CharField(max_length=200, verbose_name="название продукта")
    description = models.TextField(verbose_name="описание продукта")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена продукта"
    )
    slug = models.SlugField(unique=True)
    image_small = models.ImageField(
        upload_to="products/small/",
        **NULLABLE,
        verbose_name="маленькое изображение " "продукта"
    )
    image_medium = models.ImageField(
        upload_to="products/medium/",
        **NULLABLE,
        verbose_name="среднее изображение " "продукта"
    )
    image_large = models.ImageField(
        upload_to="products/large/",
        **NULLABLE,
        verbose_name="большое изображение " "продукта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def save(self, *args, **kwargs):
        """Генерирует slug на основе имени"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
