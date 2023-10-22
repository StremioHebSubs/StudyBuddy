from django import forms

from base.models import Message


class MessageSubmitForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your message here...'}))

    class Meta:
        model = Message
        fields = ['body']
