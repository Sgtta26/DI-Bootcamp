from django import forms
from .models import Customer, Vehicle, Rental
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        exclude = ['date_created']

class RentalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'
        widgets = {
            'rental_date': forms.DateTimeInput(attrs={'class':'my_class1', 'type':'date', 'id': 'd1'}),
            'return_date': forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'})
        }
        
    def clean_return_date(self): # happens when form.is_valid() is called
        return_date = self.cleaned_data['return_date'] # takes data from specific field (return_date) and converts it to it's type
        # Two types of dates in python: timezone aware and timezone not aware
        rental_date = self.cleaned_data['rental_date']

        if return_date <= timezone.now():
            raise ValidationError(message="Return date cannot be earlier than NOW!")

        if return_date <= rental_date:
            raise ValidationError(message="Return date cannot be before RENTAL DATE!")
            
        return return_date