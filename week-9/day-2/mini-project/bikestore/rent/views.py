from django.shortcuts import render
# from .models import Custumer
from .forms import CustumerForms, VehicleForm, RentalForm


# Create your views here.

def add_custumer(request):

    custumer_form = CustumerForms()
    context = {'form':custumer_form}

    if request.method == 'POST':
        filled_form = CustumerForms(request.POST)

        if filled_form.is_valid():
            filled_form.save()
        else:
            context ['errors'] = filled_form.errors
            # context = {'errors': filled_form.errors}
            # print(filled_form.errors)

    context = {'form':custumer_form}
    return render(request, 'add_custumer.html', context)


def add_vehicle(request):

    vehicle_form = VehicleForm()
    context = {'form':vehicle_form}

    if request.method == 'POST':
        filled_form = VehicleForm(request.POST)

        if filled_form.is_valid():
            filled_form.save()
        else:
            context ['errors'] = filled_form.errors
            # context = {'errors': filled_form.errors}
            # print(filled_form.errors)

    context = {'form':vehicle_form}
    return render(request, 'add_vehicle.html', context)




def add_rental(request):

    rental_form = RentalForm()
    context = {'form':rental_form}

    if request.method == 'POST':
        filled_form = RentalForm(request.POST)

        if filled_form.is_valid():
            filled_form.save()
        else:
            context ['errors'] = filled_form.errors
            # context = {'errors': filled_form.errors}
            # print(filled_form.errors)

    context = {'form':rental_form}
    return render(request, 'add_rental.html', context)




# def all_custumers(request):
#     custumers = Custumer.objects.all()
#     context = {'custumers':custumers}
#     return render(request, 'all_custumers.html', context)

# def name(request):
#     customer = Custumer.objects.all().order_by('first_name')
#     context = {'custumer':customer}
#     return render(request, 'all_custumers.html', context)
