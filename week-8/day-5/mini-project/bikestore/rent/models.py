from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Custumer (models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    phone_number = PhoneNumberField(blank = True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class Vehicle_Type (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vehicle_Size (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vehicle (models.Model):

    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.ForeignKey(Vehicle_Size, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_type}, {self.size}'



class Rental (models.Model):
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    customer = models.ForeignKey(Custumer, on_delete = models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete = models.PROTECT)

    def __str__(self):
        return f'{self.rental_date}, {self.customer.first_name}'



class Rental_Rate (models.Model):
    daily_rate = models.DecimalField(max_digits=4, decimal_places=2)
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete = models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_Size, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_type.name}, {self.vehicle_size.name},{self.daily_rate}'
