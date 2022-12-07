from django.shortcuts import render
from .models import Person
# from .form import 

# Create your views here.


def phone_number(request):
    # all_info = Person.objects.filter(phone_number).all()
    all_info = Person.objects.all()
    context = {'person': all_info}
    return render (request, 'person.html', context)


def name(request,name):
    info = Person.objects.filter(name=name)
    context = {'name': info}
    return render (request, 'name.html', context)