"""
Django ASGI Configuration

This module configures the ASGI (Asynchronous Server Gateway Interface) application for a Django project. It sets the 
`DJANGO_SETTINGS_MODULE` environment variable to specify the project's settings module and gets the ASGI application 
object using `get_asgi_application()` from `django.core.asgi`.

ASGI is a standard interface between web servers and Python web applications or frameworks that allows handling 
asynchronous HTTP requests, making it suitable for real-time applications and websockets.

For more information on Django ASGI, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybuddy.settings')
app = get_asgi_application()
