from django import forms
from .models import Employee, Ticket, Machine, Email
from deusto11_nexus_components.widgets.formWidgets import DateInput

""" All forms by ModelForm"""
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'email' : forms.EmailInput(),
            'description' : forms.Textarea(),
            'resolution_date' : DateInput(),
            'comment' : forms.Textarea(),
            'password' : forms.PasswordInput(),
            'ticket' : forms.Select()
        }
        labels = {
            "dni" : "DNI ej:",
            "name" : "Nombre del empleado",
            "surname" : "Apellido del empleado",
            "email" : "Email del emplado ej",
            "telefone_number" : "Numero de telefono (11 numeros, internacional) ej",
            "user_nick" : "Inserta el nick para la autenticación",
            "password" : "Contaseña",
            "ticket" : "Selecciona uno o mas tickets para empezar"
        }
    
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
            'starting_date' : DateInput(),
            'resolution_date' : DateInput(),
            'comment' : forms.Textarea(),
            'description' : forms.Textarea(),
            'machine' : forms.Select()
        }
        labels = {
            "reference_number" : "Introduce el numero de referencia",
            "title" : "Introduce el titulo de la incidencia",
            "description" : "Descripción de la incidencia",
            "starting_date" : "Fecha de inicio",
            "resolution_date" : "Fecha de resolucion",
            "urgency_level" : "Nivel de urgencia (1-3)",
            "ticket_type" : "Tipo de incidencia",
            "status" : "Estado actual de la indicencia (Activo - No activo)",
            "comment" : "Comentarios",
            "machine" : "Selecciona una o mas maquians",
        }

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"
        widgets = {
            'set_number' : forms.NumberInput(),
            'get_date' : DateInput(),
            'start_up_date' : DateInput(),
            'floor_on_premise' : forms.NumberInput(),
        }
        labels = {
            "set_number" : "Numero de serie de de la maquina",
            "model" : "Introduce el modelo",
            "brand" : "Introduce la marca de ese modelo",
            "machine_type" : "Tipo de máquina averiada",
            "get_date" : "Fecha de reconocimiento de máquina",
            "start_up_date" : "Fecha de puesta en marcha",
            "provider_name" : "Nombre del proveedor",
            "provider_telefone" : "Numero de telefono del proveedor (11 numeros, internacional)",
            "floor_on_premise" : "Planta de la fabrica donde se encuentra ",
        }
        
class EmployerLoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['dni', 'name', 'surname', 'email', 'telefone_number', 'ticket']
        

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        widgets = {
            'description' : forms.Textarea()
        }
        labels = {
            "subjct" : "Asunto",
            "description" : "Descripcion",
            "send_user" : "Pon tu email",
            "receive_user" : "Email del destinatario",
        }