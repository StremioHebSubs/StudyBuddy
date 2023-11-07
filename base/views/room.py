"""
Room and Message Views

This module defines several Django views for handling rooms and messages. These views include room creation, updating, deletion, and
displaying messages within a room. Users can also post messages in a room if they are logged in. The views are protected by the
`@login_required` decorator to ensure that only authenticated users can access them.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from typing import Union
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.models import Message, Room
from base.forms import MessageSubmitForm, RoomForm


def room(request, pk) -> Union[render, redirect]:
    form = MessageSubmitForm(request.POST or None)
    
    roomObject = Room.objects.get(id=pk)
    roomMessages = Message.objects.filter(room=roomObject)
    roomParticipants = roomObject.participants.all()
    
    if roomObject is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')
    
    if request.method == 'POST':
        if request.user is None:
            messages.error(request, 'You must be logged in to post a message')
            return redirect('login')
        
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = roomObject
            message.save()

            roomObject.participants.add(request.user)
            
            messages.success(request, 'Your message has been successfully posted')
            return redirect('room', pk=pk)
        
        
        messages.info(request, 'Sorry, but we were unable to post your message at this time. Please review your information and try again')
        return redirect('room', pk=pk)

    context = {'room': roomObject, 'roomMessages': roomMessages, 'roomParticipants': roomParticipants}
    return render(request, 'base/pages/room.html', context)


@login_required
def roomRegistration(request) -> Union[render, redirect]:
    form = RoomForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            roomObject = form.save(commit=False)
            roomObject.host = request.user
            roomObject.save()

            messages.success(request, 'Your room has been successfully created')
            return redirect('room', pk=roomObject.id)
        
        for field, errorMessage in form.errors.items():
            form.fields[field].error_messages = [errorMessage]

        messages.info(request, 'Sorry, but we were unable to create your room at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Create'}
    return render(request, 'base/forms/room/registration.html', context)


@login_required
def roomUpdate(request, pk) -> Union[render, redirect]:
    roomObject = Room.objects.get(id=pk)
    form = RoomForm(request.POST or None, instance=roomObject)

    if roomObject is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')

    if request.user != roomObject.host:
        messages.error(request, f'You are not authorized to update "{roomObject.host.username}" room')
        return redirect('room', pk=pk)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your room has been successfully updated')
            return redirect('room', pk=pk)

        for field, errorMessage in form.errors.items():
            form.fields[field].error_messages = [errorMessage]

        messages.info(request, 'Sorry, but we were unable to update your room at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Update', 'room': roomObject}
    return render(request, 'base/forms/room/registration.html', context)


@login_required
def roomDelete(request, pk) -> Union[render, redirect]:
    roomObject = Room.objects.get(id=pk)

    if roomObject is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')
    
    if request.user != roomObject.host:
        messages.error(request, f'You are not authorized to delete "{roomObject.host.username}" room')
        return redirect('room', pk)

    if request.method == 'POST':
        roomObject.delete()
        
        messages.success(request, 'Your room has been successfully deleted')
        return redirect('home')

    context = {'object': roomObject}
    return render(request, 'base/pages/delete.html', context)
