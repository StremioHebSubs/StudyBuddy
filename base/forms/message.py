"""
Message Submission Form

This module defines a form for submitting messages in the StudyBuddy Base application.
It utilizes Django's ModelForm to create a form for the 'Message' model.

The form includes a 'body' field, allowing users to input their messages with a placeholder.

For more information on creating forms with Django, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/topics/forms/
"""
from django import forms

from base.models import Message


class MessageSubmitForm(forms.ModelForm):
    """
    Message Submission Form

    This module defines a form for submitting messages in the StudyBuddy Base application.
    It utilizes Django's ModelForm to create a form for the 'Message' model.

    The form includes a 'body' field, allowing users to input their messages with a placeholder.
    """
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your message here...'}))

    class Meta:
        """
        Meta Configuration for Message Submission Form

        The 'Meta' class provides configuration options for the 'MessageSubmitForm.'
        It specifies the model associated with the form and the fields to include in the form.
        """
        model = Message
        fields = ['body']
