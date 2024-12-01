from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    """Кастомный пагинатор для приложения продуктов"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10
