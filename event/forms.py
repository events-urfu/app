from django import forms
from .models import Event, Profile

class CreateEventForm(forms.Form):
    class Meta:
        model = Event
        labels = {
            
        }
