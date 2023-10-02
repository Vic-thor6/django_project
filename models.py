from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    imagen=models.IntegerField()
    
    def __str__(self):
        return self.nombre


class CarritoCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField('Producto')
