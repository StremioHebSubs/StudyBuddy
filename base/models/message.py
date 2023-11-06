"""
Message Model for StudyBuddy

This module defines the 'Message' model for the StudyBuddy Base application. Messages are associated with users and rooms
and include a 'body' field to store the message content. The 'created' field records the message creation time.

The model allows for message ordering based on creation time, ensuring the most recent messages appear first.

For more information on defining models with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/db/models/
"""
from django.db import models

from .room import Room
from .user import User


class Message(models.Model):
    """
    Message Model for StudyBuddy

    This module defines the 'Message' model for the StudyBuddy Base application. Messages are associated with users and rooms
    and include a 'body' field to store the message content. The 'created' field records the message creation time.

    The model allows for message ordering based on creation time, ensuring the most recent messages appear first.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body.__str__()
    
    class Meta:
        """
        Meta Configuration for the Message Model

        The 'Meta' class provides configuration options for the 'Message' model.
        It specifies the default ordering of messages based on their creation time, ensuring
        the most recent messages appear first in query results.
        """
        ordering = ['-created']
    