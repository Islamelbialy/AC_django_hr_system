from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
   return HttpResponse("<h1>hello world</h1>")

def view(request):
   return HttpResponse("<h1>view 2</h1>")