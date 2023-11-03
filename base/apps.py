"""
StudyBuddy Base App Configuration

This module configures the 'base' app for the StudyBuddy Django project.
It specifies the default auto field and the app's name.

The 'base' app serves as the core of the StudyBuddy project and handles essential functionality.

For more information on Django app configuration, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/ref/applications/
"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    Django Application Configuration for 'base'

    This class represents the configuration for the 'base' Django application. It provides settings and metadata specific
    to the 'base' app, such as the default auto field for model creation.

    Attributes:
        default_auto_field (str): The default auto field used for creating models within the 'base' app.
        name (str): The name of the 'base' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
