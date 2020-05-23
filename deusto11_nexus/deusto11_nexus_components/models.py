from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

""" All class models by model.Model """
class Machine(models.Model):
    set_number = models.IntegerField(null=False, blank=False, default=0, unique=True)
    model = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    machine_type = models.CharField(max_length=100)
    get_date = models.DateField()
    start_up_date = models.DateField()
    provider_name = models.CharField(max_length=50)
    provider_telefone = PhoneNumberField(null=False, blank=False, unique=True, default="+41520000000")
    floor_on_premise = models.IntegerField()

    def __str__(self):
        return f" {self.brand} --> {self.model} de tipo {self.machine_type} en la planta={self.floor_on_premise}"

class Ticket(models.Model):
    reference_number = models.IntegerField(null=False, blank=False, default=0, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    starting_date = models.DateField()
    resolution_date = models.DateField()
    urgency_level = models.CharField(max_length=50)
    ticket_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000)
    machine = models.ManyToManyField(Machine) 

    def __str__(self):
        return f" {self.title}, urgencia: {self.urgency_level} --> tipo: {self.ticket_type}, estado: {self.status}, con equipos: {' / '.join(machine.model for machine in self.machine.all())}"

class Email(models.Model):
    send_user = models.IntegerField()
    receive_user = models.IntegerField()
    subjct = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f" usuario_emisor={self.send_user}, usuario_recibe={self.receive_user}, asunto={self.subjct}, descripcion={self.description}"

class Employee(models.Model):
    dni = models.CharField(max_length=9, null=False, blank=False, default="XXXXXXXXR", unique=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=8)
    email = models.CharField(max_length=20, default="nombre@dominio.com")
    telefone_number = PhoneNumberField(null=False, blank=False, unique=True, default="+41520000000")
    user_nick = models.CharField(max_length=10, null=False, blank=False, default="XXX", unique=True)
    password = models.CharField(max_length=20, null=False, blank=False, default="XXX")
    ticket = models.ManyToManyField(Ticket)
    # image = models.

    def __str__(self):
        return f" dni={self.dni}, nombre={self.name}, apellidos={self.surname}, email={self.email}, telefono={self.telefone_number}, nick={self.user_nick}, contrasena={self.password}, tickets = {' / '.join(ticket.title for ticket in self.ticket.all())}"

class EmployerLoginModel(models.Model):
    user_nick = models.CharField(max_length=10, null=False, blank=False, default="user")
    password = models.CharField(max_length=20, null=False, blank=False, default="password")


