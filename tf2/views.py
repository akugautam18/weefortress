# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context




# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def team_detail(request, team_id):
    return HttpResponse("Team id is %s." % team_id)


def test(request):
    return render(request, 'test.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def login(request):
    return render(request, 'login.html', {})

def about(request):
    return render(request, 'about.html', {})    

def portfolio(request):
    return render(request, 'portfolio.html', {})

def service(request):
    return render(request, 'service.html', {})      
