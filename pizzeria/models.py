from pyclbr import Class
from django.db import models

# Create your models here.

class Ventas(models.Model):
    pedido = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    celular = models.IntegerField(null=False)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'pizzeria_ventas'