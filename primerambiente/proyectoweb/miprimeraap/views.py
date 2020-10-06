from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola desde jango ...")

def primera(request):
    return HttpResponse("Otra Página ...")

def segunda(request):
    return HttpResponse("para GitHub")
