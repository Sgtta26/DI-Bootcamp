from django.contrib import admin
from .models import Vehicle,Custumer,Vehicle_Size,Vehicle_Type,Rental,Rental_Rate


# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Custumer)
admin.site.register(Vehicle_Size)
admin.site.register(Vehicle_Type)
admin.site.register(Rental)
admin.site.register(Rental_Rate)
