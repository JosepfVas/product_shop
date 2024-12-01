from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsAdmin, IsOwnerOrAdmin
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


# User Views
class UserCreateAPIView(CreateAPIView):
    """Создание пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Список всех пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]


class UserRetrieveAPIView(RetrieveAPIView):
    """Вывод одного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class UserUpdateAPIView(UpdateAPIView):
    """Обновление пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class UserDeleteAPIView(DestroyAPIView):
    """Удаление пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
