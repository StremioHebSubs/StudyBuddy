"""
URL Patterns for Django Project

This module defines the URL patterns for a Django project, including the admin interface and patterns included from the 
'base.urls' module. It specifies how URLs should be mapped to views or other URL patterns within the project.

The 'admin.site.urls' pattern directs requests to the Django admin interface, allowing administrators to manage the 
application's data.

The empty path ('') is included from the 'base.urls' module, which means that the project's main URL patterns are 
defined in the 'base' app.

For more information on defining URL patterns in Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('base.urls')),
]
