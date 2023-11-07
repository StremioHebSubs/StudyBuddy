"""
User Management Views

This module defines Django views for user registration, login, logout, and profile management. These views handle user-related actions,
such as registration, authentication, profile updates, and user profile display.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from typing import Union
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from base.models import Message, Room, Topic, User
from base.forms import UserRegistrationForm, UserLoginForm, UserUpdateForm


def userRegistration(request) -> Union[render, redirect]:
    form = UserRegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            messages.success(request, "Welcome!, it's great to have you here")
            return redirect('home')

        for field, errorMessage in form.errors.items():
            form.fields[field].error_messages = [errorMessage]

        messages.info(request, 'Sorry, but we were unable to register you at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Register'}
    return render(request, 'base/forms/user/registration.html', context)


def userLogin(request) -> Union[render, redirect]:
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        messages.success(request, "Welcome back!, it's great to have you here")
        return redirect('home')

    if request.method == 'POST':
        user = form.validateLogin(request)

        if user:
            login(request, user)
            
            messages.success(request, "Welcome back!, it's great to have you here")
            return redirect('home')
    
        for field, errorMessage in form.errors.items():
            form.fields[field].error_messages = [errorMessage]

        messages.info(request, 'Sorry, but we were unable to log you in at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Login'}
    return render(request, 'base/forms/user/login.html', context)


@login_required
def userLogout(request) -> redirect:
    logout(request)
    
    messages.success(request, "Thank you for visiting! You're now logged out. Come back soon")
    return redirect('home')


def userProfile(request, pk) -> Union[render, redirect]:
    user = User.objects.get(id=pk)

    if user is None:
        messages.info(request, 'Sorry, but we were unable to find the user you were looking for')
        return redirect('home')
    
    userRooms = Room.objects.filter(host=user)
    userTopics = Topic.objects.filter(room__in=userRooms).distinct()
    userMessages = Message.objects.filter(user=user).distinct()
    roomCounter = Room.objects.filter(topic__in=userTopics).count()

    context = {'user': user, 'topics': userTopics, 'rooms': userRooms, 'roomMessages': userMessages, 'roomCounter': roomCounter}
    return render(request, 'base/pages/profile.html', context)


@login_required
def userUpdateProfile(request) -> Union[render, redirect]:
    form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your profile has been successfully updated')
            return redirect('user-profile', pk=request.user.id)
    
        for field, errorMessage in form.errors.items():
            form.fields[field].error_messages = [errorMessage]

        messages.info(request, 'Sorry, but we were unable to update your profile at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Update'}
    return render(request, 'base/forms/user/update.html', context)
