from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField()



class Animal(models.Model):

    legs = models.IntegerField()
    weight = models.IntegerField()
    heigth = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family)
