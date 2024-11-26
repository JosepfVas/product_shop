from rest_framework.serializers import ModelSerializer
from products.models import Category, Subcategory, Product


class CategorySerializer(ModelSerializer):
    """Сериализатор категорий"""
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(ModelSerializer):
    """Сериализатор подкатегорий"""
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    """Сериализатор продуктов"""
    class Meta:
        model = Product
        fields = '__all__'
