from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from authentication.managers import CustomUserManager
from backend.base_model import BaseModel


class User(AbstractBaseUser, BaseModel):
    username = None
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class TokenBlacklist(BaseModel):
    token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.token
