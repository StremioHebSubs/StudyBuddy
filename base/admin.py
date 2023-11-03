"""
Django Admin Configuration

This module configures the Django admin panel for the StudyBuddy application.
It registers the User, Room, Topic, and Message models to be managed through the admin interface.

To access and manage these models via the Django admin panel, log in with appropriate admin credentials.

For more information on Django admin, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/ref/contrib/admin/
"""
from django.contrib import admin

from .models import User, Room, Topic, Message


admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
