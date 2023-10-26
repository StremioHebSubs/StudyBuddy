from django.db.models import Q
from django.shortcuts import render

from base.models import Room, Topic, Message


def home(request):
    topics = Topic.objects.all()[0:5]

    roomQuery = request.GET.get('query', '')
    roomMessages = Message.objects.filter(room__topic__name__icontains=roomQuery)
    roomCounter = Room.objects.filter(topic__name__icontains=roomQuery).count()
    matchedRooms = Room.objects.filter(
        Q(name__icontains=roomQuery) |
        Q(description__icontains=roomQuery) |
        Q(topic__name__icontains=roomQuery)
    )

    context = {'topics': topics, 'rooms': matchedRooms, 'roomMessages': roomMessages, 'roomCounter': roomCounter}
    return render(request, 'base/pages/home.html', context)
