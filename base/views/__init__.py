"""
Django Views

This module imports various views used in a Django project. These views handle different aspects of the application, 
including displaying the home page, topic page, user registration and profile, room creation and management, activity feed, 
and message handling. Each view is responsible for a specific part of the application's functionality.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from .activity import activity
from .home import home
from .message import messageDelete
from .room import room, roomRegistration, roomUpdate, roomDelete
from .topic import topics
from .user import userRegistration, userLogin, userLogout, userProfile, userUpdateProfile
