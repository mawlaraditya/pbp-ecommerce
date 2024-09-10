from django.shortcuts import render
from django.http import HttpResponse
from .models import Hat

def home (request) :
    hat = Hat.objects.all()
    return render(request, 'home.html', {'hat' : hat})