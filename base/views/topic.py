from django.shortcuts import render

from base.models import Room, Topic


def topics(request):
    query = request.GET.get('query', '')
    
    topics = Topic.objects.filter(name__icontains=query)
    roomCounter = Room.objects.filter(topic__name__icontains=query).count()
    
    context = {'topics': topics, 'roomCounter': roomCounter}
    return render(request, 'base/pages/topic.html', context)
