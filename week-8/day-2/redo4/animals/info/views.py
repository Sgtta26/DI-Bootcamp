from django.shortcuts import render
from .models import *

# Create your views here.

def show_family(request,id):
    family = Family.objects.get(id=id)
    return render(request, 'family.html',{'family':family})


def show_animal(request,id):
    animal = Animal.objects.get(id=id)
    return render(request, 'animal.html',{'animal':animal})


def show_animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html',{'animals':animals})