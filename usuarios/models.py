# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

class Datousuario(models.Model):
    usuario= models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    #imagen= models.ImageField(upload_to='usuarios/%Y/%m/%d', blank=True, null=True)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField(blank=True, null=True)
    pais= models.CharField(max_length=50, blank=True)
    fecha_nacimiento= models.CharField(max_length=50, blank=True)
    # esta logica se podria aplicar para un modulo de empleados para cheqeuar asistencias
    def __str__(self):
        return self.usuario.username
    