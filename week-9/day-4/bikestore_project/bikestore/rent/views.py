from django.shortcuts import render
from .forms import CustomerForm, VehicleForm, RentalForm
from django.views.generic import CreateView
# Create your views here.

# def add_customer(request):

#     customer_form = CustomerForm()
    # context = {'form':customer_form}
    
    # if request.method == 'POST':
    #     filled_form = CustomerForm(request.POST)
    #     if filled_form.is_valid():
    #         filled_form.save()
    #     else:
    #         context['errors'] = filled_form.errors
    
    # return render(request, 'add_customer.html', context)


# # /rent/vehicle/add – provide a form to add a new vehicle.

# def add_vehicle(request):

#     vehicle_form = VehicleForm()
#     context = {'form':vehicle_form}
    
#     if request.method == 'POST':
#         filled_form = VehicleForm(request.POST)
#         if filled_form.is_valid():
#             filled_form.save()
#         else:
#             context['errors'] = filled_form.errors
    
#     return render(request, 'add_vehicle.html', context)


# def add_rental(request):

#     rental_form = RentalForm()
#     context = {'form':rental_form}
    
#     if request.method == 'POST':
#         filled_form = RentalForm(request.POST)
#         if filled_form.is_valid():
#             filled_form.save()
#         else:
#             context['errors'] = filled_form.errors
    
#     return render(request, 'add_rental.html', context)

class AddCustumerView(CreateView):
    from_class = CustomerForm
    template_name = 'add_customer.html'
    success_url = './'


class AddVehicleView(CreateView):
    from_class = VehicleForm
    template_name = 'add_vehicle.html'
    success_url = './'

class AddRentalView(CreateView):
    from_class = RentalForm
    template_name = 'add_rental.html'
    success_url = './'