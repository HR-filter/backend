from django.contrib.auth.models import AbstractUser
from django.db import models

from core.texts import (
    NAME_LEN,
    MAIL_LEN,
)
from .validators import validate_not_me, UsernameValidator


class User(AbstractUser):
    email = models.EmailField(
        "Электронная почта",
        max_length=MAIL_LEN,
        unique=True,
    )

    username = models.CharField(
        "Имя пользователя",
        max_length=NAME_LEN,
        unique=True,
        db_index=True,
        validators=[
            validate_not_me,
            UsernameValidator,
        ],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
    )

    first_name = models.CharField(
        "Имя",
        max_length=NAME_LEN,
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=NAME_LEN,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("username", "email"), name="unique_username_email"
            )
        ]

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def __str__(self):
        return self.get_full_name()
