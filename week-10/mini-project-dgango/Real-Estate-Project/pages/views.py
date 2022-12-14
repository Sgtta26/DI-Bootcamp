from django.shortcuts import render
from django.http import HttpResponse
from listing.choices import bedroom_choices, state_choices, price_choices

from listing.models import Listing 
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) [:3]
    context = {
        'listings': listings,

        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
    return render (request, 'pages/home.html', context)


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')
  
    mvp_realtors = Realtor.objects.all(). filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp _realtors':mvp_realtors,
    }
    return render (request, 'pages/about.html', context)