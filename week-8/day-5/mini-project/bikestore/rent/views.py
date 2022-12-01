from django.shortcuts import render
from .models import Custumer
# Create your views here.

def all_custumers(request):
    custumers = Custumer.objects.all()
    context = {'custumers':custumers}
    return render(request, 'all_custumers.html', context)

def name(request):
    customer = Custumer.objects.all().order_by('first_name')
    context = {'custumer':customer}
    return render(request, 'all_custumers.html', context)
