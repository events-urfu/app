from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from social_django.models import AbstractUserSocialAuth, DjangoStorage, USER_MODEL
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserSocialAuth(AbstractUserSocialAuth):
    user = models.ForeignKey(USER_MODEL, related_name='custom_social_auth',
                             on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=11, blank=True)

class CustomDjangoStorage(DjangoStorage):
    user = CustomUserSocialAuth

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return str(self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to=settings.MEDIA_URL, blank=True)
    #pb_id = models.ForeignKey('Subdivision', on_delete=models.CASCADE, parent_link=True, null=True)

    def __str__(self):
        return str(self.title)


class Subdivision(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Participant(models.Model):
    STATUS = ((1, "+"), (2, "-"), (3, "None"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, parent_link=True)

    def __str__(self):
        return str(self.user.__str__())



class PBMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pb_id = models.ForeignKey(Subdivision, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user.__str__())

