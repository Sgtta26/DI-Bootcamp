from django.shortcuts import render
from models import Person

# Create your views here.


def phone_number(request):
    all_info = Person.objects.filter(phone_number).all()


def name(request):
    info = Person.objects.filter(name).all()