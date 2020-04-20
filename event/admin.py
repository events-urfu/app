from django.contrib import admin
from .models import Event, Participant, Subdivision, PBMember
# Register your models here.

class ParticipantInline(admin.TabularInline):
    model = Participant
    fields = ('user', 'status')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]
    exclude = ['participants']


@admin.register(PBMember)
class PBMemberAdmin(admin.ModelAdmin):
    list_filter = ['pb_id']

admin.site.register(Participant)
admin.site.register(Subdivision)