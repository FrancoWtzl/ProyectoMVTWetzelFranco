from django.db import models

# Create your models here.


class FliaWetzel(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    año_nacimiento=models.IntegerField() 
