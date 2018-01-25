# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Team, Game, Team_user, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'team', 'event_type', 'event_info', 'date_time')
    search_fields = ('title', 'event_info', 'game', 'description')

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Team_user)
admin.site.register(Event, EventAdmin)

