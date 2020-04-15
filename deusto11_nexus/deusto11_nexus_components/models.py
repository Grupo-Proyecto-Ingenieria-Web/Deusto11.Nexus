from django.db import models

# Create your models here.
class Employee(models.Model):
    dni = models.CharField(max_length=9, null=True, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    email = models.CharField(max_length=80)
    telefone_number = models.IntegerField()

    def __str__(self):
        return f"id={self.id}, dni={self.dni}, nombre={self.name}, apellidos={self.surname}, email={self.email}, telefono={self.telefone_number}"

#clase de tickets
class Ticket(models.Model):
    reference_number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    starting_date = models.DateField()
    resolution_date = models.DateField()
    urgency_level = models.CharField(max_length=50)
    ticket_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"id={self.id}, numero_referencia={self.reference_number}, titulo={self.title}, descripcion={self.description}, fecha_apertura={self.starting_date}, fecha_resolucion={self.resolution_date}, nivel_urgencia={self.urgency_level}, tipo={self.ticket_type}, estado={self.status}, empleado={self.employee}, comentario={self.comment}"
#clase equipo
class Machine(models.Model):
    set_number = models.IntegerField(null=True, blank=True)
    model = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    machine_type = models.CharField(max_length=100)
    get_date = models.DateField()
    start_up_date = models.DateField()
    provider_name = models.CharField(max_length=50)
    provider_telefone = models.IntegerField()
    floor_on_premise = models.IntegerField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id}, numero_serie={self.set_number}, modelo={self.model}, marca={self.brand}, tipo_equipo={self.machine_type}, fecha_adquisicion={self.get_date}, fecha_puesta_en_marcha={self.start_up_date}, proveedor_nombre={self.provider_name}, proveedor_telefono={self.provider_telefone}, planta={self.floor_on_premise}, ticket={self.ticket}"


