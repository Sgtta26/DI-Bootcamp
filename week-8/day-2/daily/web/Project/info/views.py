from django.shortcuts import render
from django.db import models
from .models import Person

# Create your views here.


def get_name(request,name):
    person = Person.objects.get(name = name)
    return render(request, 'info.html', {'person': Person})


def get_number(request,number):
    number = Person.objects.get(phone_number = number)
    return render(request, 'info.html', {'person': Person})
