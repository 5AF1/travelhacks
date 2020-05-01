from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour,Spot
# Create your views here.

def index(response,i):
    tt=Tour.objects.get(id=i)
    ts = tt.spot_set.get(id = 1)
    return HttpResponse("<h1>%s <br>%s</h1>"%(tt.name,ts.name))

def intro(response):
    return HttpResponse("<h1>Hi</h1>")
