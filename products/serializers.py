from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from products.models import Category, Subcategory, Product


class CategorySerializer(ModelSerializer):
    """Сериализатор категорий"""

    class Meta:
        model = Category
        fields = "__all__"


class SubcategorySerializer(ModelSerializer):
    """Сериализатор подкатегорий"""

    class Meta:
        model = Subcategory
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    """Сериализатор продуктов"""

    category = CharField(source="subcategory.category.name", read_only=True)
    subcategory = CharField(source="subcategory.name", read_only=True)
    all_images = SerializerMethodField()

    class Meta:
        model = Product
        fields = ["name", "slug", "category", "subcategory", "price", "all_images"]

    def get_all_images(self, obj):
        """Собирает все изображения в один список"""
        images = []
        for field_name in ["image_small", "image_medium", "image_large"]:
            image_field = getattr(obj, field_name)
            if image_field:
                images.append(image_field.url)
        return images
