from django.db import models

# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    adress = models.CharField(max_length=200)