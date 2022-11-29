from django.shortcuts import render
from .models import Family, Animal

# Create your views here.

def family(request, id):
    context = Family.object.get(id = id)
    return render(request, 'family.html', {'Family':family})


def animal(request,id):

    context = Animal.objects.get(id = id)
    return render(request, 'animal.html', {'Animal':animal})


def animals(request,id):

    context = Animal.objects.all()
    return render(request, 'animals.html', {'Animal':animals})