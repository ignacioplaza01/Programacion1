from django.db import models

# Create your models here.

class Juguetes(models.Model):
    marca = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    producto = models.CharField(max_length=20)
    edad = models.CharField(max_length=10)
    precio = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=5)
