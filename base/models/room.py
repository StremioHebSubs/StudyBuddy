"""
Room Model for StudyBuddy

This module defines the 'Room' model for the StudyBuddy Base application. Rooms are associated with hosts and topics
and include attributes such as 'name,' 'description,' and 'participants.' 

The model allows for ordering of rooms based on update and creation times.

For more information on defining models with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/db/models/
"""
from django.db import models

from .topic import Topic
from .user import User


class Room(models.Model):
    """
    Room Model for StudyBuddy

    This module defines the 'Room' model for the StudyBuddy Base application. Rooms are associated with hosts and topics
    and include attributes such as 'name,' 'description,' and 'participants.' 

    The model allows for ordering of rooms based on update and creation times.
    """
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name.__str__()
    
    class Meta:
        """
        Meta Configuration for the Room Model

        The 'Meta' class provides configuration options for the 'Room' model.
        It specifies the default ordering of rooms based on their update and creation times.
        Rooms are ordered by the most recently updated and created rooms.
        """
        ordering = ['-updated', '-created']
