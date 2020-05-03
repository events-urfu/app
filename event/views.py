import json
from rest_framework import viewsets, permissions, exceptions
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail

from .models import Event, Participant
from .serializers import EventsSerializer, InstanceSerializer
from .paginators import StandardResultsSetPagination

class ViewSetEvent(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = InstanceSerializer(queryset)
        return Response(serializer.data)

    def get_queryset(self, pk = None):
        if self.action == 'list':
            return Event.objects.all().order_by('-date')
        if self.action == 'retrieve':
            return Event.objects.get(pk=pk)
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventsSerializer
        if self.action == 'retrieve':
            return InstanceSerializer
        return EventsSerializer

def add_participant(request, event_id):
    if request.user.is_authenticated():
        pass


def send_message(request, event_id):
    if request.user.is_authenticated():
        event = Event.objects.get(pk = event_id)
        send_mail(event.title,
    'Вы успешно записались на ' + event.title,
    'urfu-events@example.com',
    [request.user.email],
    fail_silently=False,)