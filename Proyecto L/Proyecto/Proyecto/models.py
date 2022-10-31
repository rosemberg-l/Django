from django.db import connections
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=11)
    celular = models.CharField(max_length=11)
    fechanacimiento = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    cedula = models.CharField(max_length=11)
    class Meta:
        db_table='clientes'
