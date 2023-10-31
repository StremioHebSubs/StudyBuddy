from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.models import Message


@login_required
def messageDelete(request, pk):
    message = Message.objects.get(id=pk)

    if message is None:
        messages.info(request, "Sorry, but the message you are looking for doesn't exist")
        return redirect('home')
    
    if request.user != message.user:
        messages.error(request, f'You are not authorized to delete "{message.user.username}" message')
        return redirect('room', message.room.pk)
    
    if request.method == 'POST':
        message.delete()
        
        messages.success(request, 'Your message has been successfully deleted')
        return redirect('room', message.room.pk)

    context = {'object': message}
    return render(request, 'base/pages/delete.html', context)
