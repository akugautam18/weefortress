# -*- coding: utf-8 -*-
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>this is my first app</h1>")

def team_detail(request,team_id):
    return HttpResponse("Team id is %s." % team_id)
        