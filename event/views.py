from django.shortcuts import render
from rest_framework import viewsets, permissions, exceptions
from .models import Event
from .serializers import EventSerializer

# Create your views here.
def main(request):
    events = []

    return render(
        request,
        "main.html",
        {
            "events": events,
        }
    )

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('title')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create_event(self,serializer):
        admin=self.request.user
        if admin.profile.admin:
            serializer.save()
        else:
            raise PermissionDenied("You are not authorized to create Events. Update your profile!")

    def delete_event(self):
        Event_instance=self.get_object()
        user=self.request.user

        if user.is_staff:
            Event_instance.delete()
        else:
            raise ValidationError("Sorry you are not authorized to delete this Event!")