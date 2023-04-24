from pyclbr import Class
from django.db import models

# Create your models here.

class Ventas(models.Model):
    Pedidos = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    Apellido = models.CharField(max_length=30, null=False)
    Correo = models.CharField(max_length=50, null=False)
    Telefono = models.IntegerField(null=False)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)