from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def captain_america(request):
        return HttpResponse("Captain America - The First Avenger")
