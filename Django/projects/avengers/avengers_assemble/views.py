from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def avengers_assemble(request):
    val={"value":time.strftime("%d/%m/%y - %H:%M:%S")}
    return render(request,'welcome.html',context=val)
