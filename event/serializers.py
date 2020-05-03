from rest_framework import serializers
from .models import Event, User, Participant


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'title', 'date', 'place', 'image')

class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    participants_count = serializers.IntegerField(source='get_count')

    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'place', 'image', 'participants_count')


def get_count(obj):
    return Participant.objects.filter(obj.pk).count()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name',)