from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event/static/img/event_images')
    paticipants = models.ManyToManyField('Participant', blank=True)
    pb_id = models.ForeignKey('Subdivision', on_delete=models.CASCADE, parent_link=True, null=True)

    def __str__(self):
        return str(self.title)

class Subdivision(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('PBMember', blank=True)

    def __str__(self):
        return str(self.name)

class Participant(models.Model):
    STATUS = ((1, "+"), (2, "-"), (3, "None"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, parent_link=True)

    def __str__(self):
        return str(self.user.__str__())


class PBMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pb_id = models.ForeignKey(Subdivision, on_delete=models.CASCADE, parent_link=True, null=True)

    def __str__(self):
        return str(self.user.__str__())
