"""
Home Page View

This module defines a Django view for the home page. The view retrieves a list of topics and allows users to search for rooms
based on a query string. It displays topics and rooms matching the query and provides a count of matching rooms. This view is
accessible to all users.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from django.db.models import Q
from django.shortcuts import render

from base.models import Message, Room, Topic


def home(request) -> render:
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
