from django.urls import path
from products.views import (
    CategoryListAPIView,
    SubcategoryListAPIView,
    ProductListAPIView,
    ProductRetrieveAPIView,
)

urlpatterns = [
    # Category CRUD
    path("category_list/", CategoryListAPIView.as_view(), name="category_list"),
    # Subcategory CRUD
    path(
        "subcategory_list/", SubcategoryListAPIView.as_view(), name="subcategory_list"
    ),
    # Product CRUD
    path("list/", ProductListAPIView.as_view(), name="product_list"),
    path("retrieve/", ProductRetrieveAPIView.as_view(), name="product_retrieve"),
]
