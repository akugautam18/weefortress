# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render
from django.template import context
from django.template.loader import get_template


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def team_detail(request,team_id):
    return HttpResponse("Team id is %s." % team_id)


def test(request):
    return render(request, 'test.html', {})

def blog(request):
    return render(request,'blog.html',{})    
