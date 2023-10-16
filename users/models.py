from collections.abc import Iterable
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class Role(models.TextChoices):
    USER = 'user', _('User')
    MODERATOR = 'moderator', _('Moderator')
    ADMIN = 'admin', _('Admin')


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    password = models.CharField(max_length=128, blank=True)
    confirmation_code = models.CharField(max_length=6, blank=True)

    objects = CustomUserManager()


    def save(self, *args, **kwargs):
        self.is_staff = self.role in [Role.MODERATOR, Role.ADMIN]
        self.is_superuser = self.role == Role.ADMIN
        super().save(*args, **kwargs)