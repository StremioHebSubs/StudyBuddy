from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.models import Room, Message
from base.forms import RoomForm, MessageSubmitForm


def room(request, pk):
    form = MessageSubmitForm(request.POST or None)
    
    room = Room.objects.get(id=pk)
    roomMessages = Message.objects.filter(room=room)
    roomParticipants = room.participants.all()
    
    if room is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')
    
    if request.method == 'POST':
        if request.user is None:
            messages.error(request, 'You must be logged in to post a message')
            return redirect('login')
        
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            print(message)
            message.save()

            room.participants.add(request.user)
            
            messages.success(request, 'Your message has been successfully posted')
            return redirect('room', pk=pk)
        
        else:
            messages.info(request, 'Sorry, but we were unable to post your message at this time. Please review your information and try again')
            return redirect('room', pk=pk)

    context = {'room': room, 'roomMessages': roomMessages, 'roomParticipants': roomParticipants}
    return render(request, 'base/pages/room.html', context)


@login_required
def roomRegistration(request):
    form = RoomForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()

            messages.success(request, 'Your room has been successfully created')
            return redirect('room', pk=room.id)

        else:
            for field, errorMessage in form.errors.items():
                form.fields[field].error_messages = [errorMessage]

            messages.info(request, 'Sorry, but we were unable to create your room at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Create'}
    return render(request, 'base/forms/room/registration.html', context)


@login_required
def roomUpdate(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(request.POST or None, instance=room)

    if room is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')

    if request.user != room.host:
        messages.error(request, f'You are not authorized to update "{room.host.username}" room')
        return redirect('room', pk=pk)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your room has been successfully updated')
            return redirect('room', pk=pk)

        else:
            for field, errorMessage in form.errors.items():
                form.fields[field].error_messages = [errorMessage]

            messages.info(request, 'Sorry, but we were unable to update your room at this time. Please review your information and try again')

    context = {'form': form, 'button_text': 'Update', 'room': room}
    return render(request, 'base/forms/room/registration.html', context)


@login_required
def roomDelete(request, pk):
    room = Room.objects.get(id=pk)

    if room is None:
        messages.info(request, "Sorry, but the room you are looking for doesn't exist")
        return redirect('home')
    
    if request.user != room.host:
        messages.error(request, f'You are not authorized to delete "{room.host.username}" room')
        return redirect('room', pk)

    if request.method == 'POST':
        room.delete()
        
        messages.success(request, 'Your room has been successfully deleted')
        return redirect('home')

    context = {'object': room}
    return render(request, 'base/pages/delete.html', context)
