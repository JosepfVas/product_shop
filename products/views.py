from rest_framework import generics
from products.models import Category, Subcategory, Product
from products.paginators import CustomPaginator
from products.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
    """API endpoint для получения списка всех категорий"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPaginator


class SubcategoryListAPIView(generics.ListAPIView):
    """API endpoint для получения списка всех подкатегорий"""

    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    pagination_class = CustomPaginator


class ProductListAPIView(generics.ListAPIView):
    """API endpoint для получения списка всех продуктов"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """API endpoint для получения одного продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
