import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, **kwargs):
        if not username:
            username = uuid.uuid4().hex[:10]
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username=None, email=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **kwargs)


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Phone Number",
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    
    objects = CustomUserManager()