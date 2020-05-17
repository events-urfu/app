import json

from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import auth_logout
from rest_framework import viewsets, permissions, exceptions, filters
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest
from django.core.mail import send_mail
from django.shortcuts import redirect
from social_django.views import login
from json import dumps

from .models import Event, Participant, CustomUserSocialAuth, Profile, User
from .serializers import EventsSerializer, InstanceSerializer
from .paginators import StandardResultsSetPagination
from rest_framework.request import Request

class ViewSetEvent(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        serializer_context = {
            'request': request,
        }
        queryset = self.get_queryset()
        serializer = EventsSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = self.get_queryset(pk)
        serializer = InstanceSerializer(queryset)
        return Response(serializer.data)

    def get_queryset(self, pk = None, key = None):
        if self.action == 'list':
            return Event.objects.all().order_by('-date')
        if self.action == 'retrieve':
            return Event.objects.get(pk=pk)
        if self.action == 'search':
            return Event.objects.filter(title__startswith=key)
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EventsSerializer
        if self.action == 'retrieve':
            return InstanceSerializer
        return EventsSerializer

def sign_up(request):
    if request.method == "POST":
        email = request.GET.get("email")
        password = request.GET.get("password")
        if not (User.objects.filter(email=email).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(email, password)
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            raise HttpResponse(
                'Looks like a username with that email or password already exists')

def log_in(request):
    if request.method == "POST":
        user = authenticate(username=request.GET.get("email"), password=request.GET.get("password"))
        try:
            login(request, user)
            return HttpResponse("Everything is OK")
        except AttributeError:
            return redirect('/login')

def log_out(request):
    logout(request)
    return HttpResponse("You are successfully logged out")

def add_participant(request):
    data = {
        'status': False
    }
    if request.method == "POST":
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)
            profile.patronymic = request.GET.get("name").Split()[2]
            profile.group = request.GET.get("group")
            participant = Participant()
            participant.user = request.user
            participant.event_id = request.GET.get("event_id")
            participant.save()
            data["status"] = True
        return HttpResponse(dumps(data))
    return HttpResponse("This URL shouldn't be accessed with web browser")

def send_message(request):
    if request.user.is_authenticated():
        event = Event.objects.get(pk = request.GET.get("event_id"))
        send_mail(event.title,
    'Вы успешно записались на ' + event.title,
    'urfu-events@example.com',
    [request.user.email],
    fail_silently=False,)
