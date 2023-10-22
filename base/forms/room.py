from django import forms

from base.models import Room, Topic


class RoomForm(forms.ModelForm):
    topic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Python'}))

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        if self.instance and hasattr(self.instance, 'topic') and self.instance.topic:
            self.initial['topic'] = self.instance.topic.name

    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

    def clean_topic(self):
        topic_name = self.cleaned_data.get('topic')
        topic = Topic.objects.get_or_create(name=topic_name)[0]

        return topic
