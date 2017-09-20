# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
from django.template import context
from django.template.loader import get_template


# Create your views here.
def index(request):
    return HttpResponse("<h1>this is my first app</h1>")


def team_detail(request,team_id):
    return HttpResponse("Team id is %s." % team_id)


def test(request):
    temp = get_template('test.html')
    response = temp.render()
    return HttpResponse(response)
