"""
Activity Page View

This module defines a Django view for the "activity" page. The view retrieves all messages from the database and displays
them on the activity page. This view is accessible to all users.

For more information on Django views, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/http/views/
"""
from django.shortcuts import render

from base.models import Message


def activity(request) -> render:
    roomMessages = Message.objects.all()[0:5]

    context = {'roomMessages': roomMessages}
    return render(request, 'base/pages/activity.html', context)
