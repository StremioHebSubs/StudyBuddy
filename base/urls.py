"""
StudyBuddy Base URL Configuration

This module defines the URL patterns for the StudyBuddy Django project.
It maps specific URLs to corresponding views and provides named URLs for easy reference.

The URLs defined here determine how different parts of the StudyBuddy application can be accessed via the web.

For more information on Django URL routing, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('topics/', views.topics, name='topics'),

    path('user/registration/', views.userRegistration, name='user-registration'),
    path('user/login/', views.userLogin, name='user-login'),
    path('user/logout/', views.userLogout, name='user-logout'),
    path('user/profile/update/', views.userUpdateProfile, name='user-update-profile'),
    path('user/profile/<str:pk>/', views.userProfile, name='user-profile'), 

    path('room/registration/', views.roomRegistration, name='room-registration'),
    path('room/<str:pk>/', views.room, name='room'),
    path('room/update/<str:pk>/', views.roomUpdate, name='room-update'),
    path('room/delete/<str:pk>/', views.roomDelete, name='room-delete'),

    path('message/delete/<str:pk>/', views.messageDelete, name='message-delete'),
    
    path('activity/', views.activity, name='activity'),
]
