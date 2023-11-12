"""
Django WSGI Configuration

This module configures the Django project for WSGI (Web Server Gateway Interface) using the 'get_wsgi_application' 
function. It sets the 'DJANGO_SETTINGS_MODULE' environment variable to 'studybuddy.settings', indicating the location of 
the project's settings module.

The 'get_wsgi_application' function initializes the Django application and allows it to be served by a WSGI-compatible 
web server.

For more information on configuring Django for WSGI, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybuddy.settings')
app = get_wsgi_application()
