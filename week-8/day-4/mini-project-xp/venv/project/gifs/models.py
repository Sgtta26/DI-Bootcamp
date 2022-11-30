from django.db import models


# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField
    




class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif, on_delete = models.CASCADE)



