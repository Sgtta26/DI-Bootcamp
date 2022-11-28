from django.shortcuts import render
import json

# Create your views here.

# with open('animal.json', 'r') as f:
#     info = json.load(f)

def get_animal(id):
    with open('animal.json', 'r') as f:
        info = json.load(f)


    animals = info['animals']

    for animal in animals:
        if animal['id'] == id:
            return animal


def animal_info(request, animal_id):

    animal = get_animal(animal_id)
    context = {'aniaml': animal}

    return render(request, 'animal.html', context)


def get_family(id):
    with open('animal.json', 'r') as f:
        info = json.load(f)

    families = info['families']

    for family in families:
        if family['id'] == id:
            return family

def family_info(request, family_id):

    family = get_family(family_id)
    context = {'family': family}

    return render(request, 'family.html', context)