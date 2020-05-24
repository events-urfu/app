from django import forms
from .models import Event

class CreateEventForm(forms.Form):
    class Meta:
        model = Event
        labels = {
            
        }
