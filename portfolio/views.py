from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse( "Hello Friend")

def contact(request):
    return HttpResponse( "Contact Me")

def greet_by_name(request, name):
    return HttpResponse(f"hello {name}")