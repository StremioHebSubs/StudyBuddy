from django.shortcuts import render

from base.models import Message


def activity(request):
    roomMessages = Message.objects.all()

    context = {'roomMessages': roomMessages}
    return render(request, 'base/pages/activity.html', context)
