from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_numer = models.CharField()
    adress = models.CharField(max_length=200)