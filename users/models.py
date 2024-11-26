from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя"""

    STATUS_SELECTION = ((True, "Действующий"), (False, "Заблокирован"))

    username = None
    fullname = models.CharField(
        max_length=150, **NULLABLE, verbose_name="Полное имя пользователя"
    )
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.PositiveIntegerField(**NULLABLE, verbose_name="телефон")
    city = models.CharField(max_length=100, **NULLABLE, verbose_name="город")
    avatar = models.ImageField(upload_to="users", **NULLABLE, verbose_name="фото")
    is_active = models.BooleanField(
        choices=STATUS_SELECTION, default=True, verbose_name="Статус пользователя"
    )
    last_login = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name="последний раз в сети"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
