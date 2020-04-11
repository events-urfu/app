from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event/static/img/event_images')
    paticipants = models.ManyToManyField(User)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    admin = models.BooleanField()
