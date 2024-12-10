from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("<h1>Connected with Django</h1> <h3>It looks good on Android Mobile</h3>")