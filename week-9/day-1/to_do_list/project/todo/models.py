from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


# Create your models here.

def validate_date(date):
    if date <= date.today():
        raise ValidationError(message="The date provided is incorrect")


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    has_been_done = models.BooleanField(default=False, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(blank=True, null=True)
    deadline_date = models.DateField(validators=[validate_date,])
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title},{self.details[:10]}'

    