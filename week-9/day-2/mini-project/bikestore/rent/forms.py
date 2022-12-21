from django import forms
from .models import Custumer,Vehicle,Rental
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustumerForms(forms.ModelForm):
    class Meta:
        model = Custumer
        field = '__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        # field = '__all__'
        exclude = ['date_created']



class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
        widgets = {
            'rental_date': forms.DateTimeInput(attrs={'class':'my_class1', 'type':'date', 'id': 'd1'}),
            'return_date': forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'})
        }
    def clean_return_date(self):
        data = self.cleaned_data['rental_date']
        print(type(data))
        if data <= timezone.now():
            raise ValidationError(message= 'return date cannot be earlier than now')
        return data

        # print("CHECKING THE RETURN DATE!")
