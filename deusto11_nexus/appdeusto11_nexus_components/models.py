from django.db import models

# Create your models here.
#Clase de empleado

class Empleado(models.Model):
    dni=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    telefono=models.IntegerField(max_length=15)
#clase de tickets
class Tickets(models.Model):
    numero_referencia=models.IntegerField(max_length=10,primary_key=True)
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    fecha_apertura=models.DateField()
    fecha_resolucion=models.DateField()
    nivel_urgencia=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    empleado=models.ManyToManyField(Empleado)
    comentario=models.ForeignKey(Empleado, on_delete=models.CASCADE)

#clase equipo
class Equipo(models.Model):
    numero_serie=models.IntegerField(max_length=10,primary_key=True)
    modelo=models.CharField(max_length=60)
    marca=models.CharField(max_length=60)
    tipo_equipo=models.CharField(max_length=100)
    fecha_adquisicion=models.DateField()
    fecha_puesta_en_marcha=models.DateField()
    proveedor_nombre=models.CharField(max_length=50)
    proveedor_telefono=models.IntegerField(max_length=15)
    planta=models.IntegerField(max_length=2)
    ticket=models.ForeignKey(Tickets, on_delete=models.CASCADE)
