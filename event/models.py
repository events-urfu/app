from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    image = models.ImageField(width_field=400, height_field=300)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    admin = models.BooleanField()
