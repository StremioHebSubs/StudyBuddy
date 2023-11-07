"""
Message Deletion View

This module defines a Django view for deleting messages. The view is protected by the `@login_required` decorator to ensure that
only authenticated users can access it. Users can delete their own messages, and upon successful deletion, they are redirected to
the room where the message was posted. Unauthorized users will be shown an error message.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from typing import Union
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.models import Message


@login_required
def messageDelete(request, pk) -> Union[render, redirect]:
    message = Message.objects.get(id=pk)

    if message is None:
        messages.info(request, "Sorry, but the message you are looking for doesn't exist")
        return redirect('home')
    
    if request.user != message.user:
        messages.error(request, f'You are not authorized to delete "{ message.user.username }" message')
        return redirect('room', message.room.pk)
    
    if request.method == 'POST':
        message.delete()
        
        messages.success(request, 'Your message has been successfully deleted')
        return redirect('room', message.room.pk)

    context = {'object': message}
    return render(request, 'base/pages/delete.html', context)
