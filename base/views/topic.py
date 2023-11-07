"""
Topics View

This module defines a Django view for displaying topics and their associated rooms. Users can search for topics, and the view lists topics
matching the search query along with a count of rooms under each topic.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from django.shortcuts import render

from base.models import Room, Topic


def topics(request) -> render:
    query = request.GET.get('query', '')
    
    topicObjects = Topic.objects.filter(name__icontains=query)
    roomCounter = Room.objects.filter(topic__name__icontains=query).count()
    
    context = {'topics': topicObjects, 'roomCounter': roomCounter}
    return render(request, 'base/pages/topic.html', context)
