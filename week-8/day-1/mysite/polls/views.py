from django.shortcuts import render
from datetime import date

# Create your views here.

def homepage(request):

    # context = {'time':'27th of November, 2022'}
    context = {'time': date.today(), 'user':'Sarah'}
    return render(request, 'homepage.html', context)


def profile(request):
    
    context = {'name':'Sarah', 'gender':'F', 'item':['banana', 'kiwi', 'apple']}
    return render(request, 'user_profile.html', context)