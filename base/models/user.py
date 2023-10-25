from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=False, null=False, default='This user has not added a bio yet.')
    avatar = models.ImageField(default='default_avatar.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
