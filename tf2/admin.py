# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Team, Games, Team_users, Events

admin.site.register(Team)
admin.site.register(Games)
admin.site.register(Team_users)
admin.site.register(Events)

