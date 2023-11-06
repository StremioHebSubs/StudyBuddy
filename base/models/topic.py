"""
Topic Model for StudyBuddy

This module defines the 'Topic' model for the StudyBuddy Base application. Topics are associated with a 'name' attribute
and record the creation time using the 'created' field. The model allows for ordering topics based on their creation time.

For more information on defining models with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/db/models/
"""
from django.db import models


class Topic(models.Model):
    """
    Topic Model for StudyBuddy

    This module defines the 'Topic' model for the StudyBuddy Base application. Topics are associated with a 'name' attribute
    and record the creation time using the 'created' field. The model allows for ordering topics based on their creation time.
    """
    name = models.CharField(max_length=20, unique=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name.__str__()
    
    class Meta:
        """
        Meta Configuration for the Topic Model

        The 'Meta' class provides configuration options for the 'Topic' model.
        It specifies the default ordering of topics based on their creation time.
        Topics are ordered by the most recently created topics.
        """
        ordering = ['-created']
