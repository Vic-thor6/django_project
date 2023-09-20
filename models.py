from django.db import models

# Create your models here.

class Project(models.Model):
    title = "titulo_imagen"


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    rut = models.CharField(max_length=15,unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    comuna_id = models.ForeignKey(Comuna, on_delete=models.CASCADE,related_name='persona')
    
    def __str__(self):
        return self.nombre
    
class usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombreUsuario
    
class producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.CharField(max_length=50)
    imagen=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre