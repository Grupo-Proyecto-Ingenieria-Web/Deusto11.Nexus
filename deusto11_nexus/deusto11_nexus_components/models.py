from django.db import models

# Create your models here.
class Empleado(models.Model):
    dni=models.CharField(max_length=9, null=True, blank=True)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=70)
    email=models.CharField(max_length=80)
    telefono=models.IntegerField()

    def __str__(self):
        return f"id={self.id}, dni={self.dni}, nombre={self.nombre}, apellidos={self.nombre}, email={self.email}, telefono={self.telefono}"

#clase de tickets
class Tickets(models.Model):
    numero_referencia=models.IntegerField(null=True, blank=True)
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    fecha_apertura=models.DateField()
    fecha_resolucion=models.DateField()
    nivel_urgencia=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    comentario=models.CharField(max_length=1000)

    def __str__(self):
        return f"id={self.id}, numero_referencia={self.numero_referencia}, titulo={self.titulo}, descripcion={self.descripcion}, fecha_apertura={self.fecha_apertura}, fecha_resolucion={self.fecha_resolucion}, nivel_urgencia={self.nivel_urgencia}, tipo={self.tipo}, estado={self.estado}, empleado={self.empleado}, comentario={self.comentario}"

#clase equipo
class Equipo(models.Model):
    numero_serie=models.IntegerField(null=True, blank=True)
    modelo=models.CharField(max_length=60)
    marca=models.CharField(max_length=60)
    tipo_equipo=models.CharField(max_length=100)
    fecha_adquisicion=models.DateField()
    fecha_puesta_en_marcha=models.DateField()
    proveedor_nombre=models.CharField(max_length=50)
    proveedor_telefono=models.IntegerField()
    planta=models.IntegerField()
    ticket=models.ForeignKey(Tickets, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id}, numero_serie={self.numero_serie}, modelo={self.modelo}, marca={self.marca}, tipo_equipo={self.tipo_equipo}, fecha_adquisicion={self.fecha_adquisicion}, fecha_puesta_en_marcha={self.fecha_puesta_en_marcha}, proveedor_nombre={self.proveedor_nombre}, proveedor_telefono={self.proveedor_telefono}, planta={self.planta}, ticket={self.ticket}"