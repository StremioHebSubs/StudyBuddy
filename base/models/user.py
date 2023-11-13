"""
User Model for StudyBuddy

This module defines the custom 'User' model for the StudyBuddy Base application, extending Django's 'AbstractUser' class.
The 'User' model includes fields for 'name,' 'username,' 'email,' 'bio,' and 'avatar.' It also specifies the 'USERNAME_FIELD'
as 'email' for authentication purposes.

For more information on customizing user models with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/auth/customizing/#using-a-custom-user-model
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User Model for StudyBuddy

    This module defines the custom 'User' model for the StudyBuddy Base application, extending Django's 'AbstractUser' class.
    The 'User' model includes fields for 'name,' 'username,' 'email,' 'bio,' and 'avatar.' It also specifies the 'USERNAME_FIELD'
    as 'email' for authentication purposes.
    """
    name = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=False, null=False, default='This user has not added a bio yet.')
    avatar = models.ImageField(default='default_avatar.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
