# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models




def __unicode__(self):
    return '%s' % (self.user)

class Team(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")

    def __unicode__(self):
        return self.title

class Game(models.Model):
    title = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=1000, default="")

    def __unicode__(self):
        return self.title


class Team_user(models.Model):
    TEAM_USERS = ((1, "Player"), (2, "Moderator"), (3, "Admin"))
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_type = models.PositiveIntegerField(choices=TEAM_USERS, default=1)

    def __unicode__(self):
        return unicode(self.user_id)

class Event(models.Model):
    TYPE = ((1, "team level"), (2, "user level"))
    title = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event_type = models.PositiveIntegerField(choices=TYPE, default=0)
    winner = models.CharField(max_length=200, default="")
    event_info = models.CharField(max_length=600, default=0)
    description = models.TextField(max_length=1000)
    date_time = models.DateField(null=True)

    def __unicode__(self):
        return self.title








