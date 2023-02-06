from django.db import models

# Create your models here.
class Parrot(models.Model):
    name = models.Charfield(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()