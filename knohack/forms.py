from django import forms

from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('event_name', 'event_theme', 'min_grade', 'max_grade',
        'event_details', 'event_contact_name', 'event_contact_phone',)
