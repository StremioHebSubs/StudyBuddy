"""
Room Creation Form

This module defines a form for creating rooms in the StudyBuddy Base application.
The form uses Django's ModelForm and includes fields for 'topic,' 'name,' and 'description.'

The 'topic' field allows users to specify the room's topic with a placeholder.
The form also ensures that the 'topic' field corresponds to an existing or newly created topic.

For more information on creating forms with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/forms/
"""
from django import forms

from base.models import Room, Topic


class RoomForm(forms.ModelForm):
    """
    Room Creation Form

    This module defines a form for creating rooms in the StudyBuddy Base application.
    The form uses Django's ModelForm and includes fields for 'topic,' 'name,' and 'description.'

    The 'topic' field allows users to specify the room's topic with a placeholder.
    The form also ensures that the 'topic' field corresponds to an existing or newly created topic.
    """
    topic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Python'}))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if self.instance and hasattr(self.instance, 'topic') and self.instance.topic:
            self.initial['topic'] = self.instance.topic.name

    def clean_topic(self) -> Topic:
        topic_name = self.cleaned_data.get('topic')
        topic = Topic.objects.get_or_create(name=topic_name)[0]

        return topic

    class Meta:
        """
        Meta Configuration for Room Creation Form

        The 'Meta' class provides configuration options for the 'RoomForm.'
        It specifies the model associated with the form and the fields to include in the form.
        """
        model = Room
        fields = ['topic', 'name', 'description']
