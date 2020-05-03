from django.contrib import admin
from .models import Event, Participant, Subdivision, PBMember
# Register your models here.

class ParticipantInline(admin.TabularInline):
    model = Participant
    fields = ('user', 'status')

class PBMembersInline(admin.TabularInline):
    model = PBMember
    fields = ('user__last_name', 'user__email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]
    exclude = ['participants']


@admin.register(PBMember)
class PBMemberAdmin(admin.ModelAdmin):
    list_filter = ['pb_id']

@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    inlines = [PBMembersInline]

admin.site.register(Participant)