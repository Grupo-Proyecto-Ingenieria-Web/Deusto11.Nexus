from django import forms
from .models import Employee, Ticket, Machine

#Para coger de esta clase los atributos de empleado
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#Para coger de esta clase los atributos de ticket
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

#Para coger de esta clase los atributos de maquina
class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"
        
#Para coger de esta clase los atributos de logear empleado
class EmployerLoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['dni', 'name', 'surname', 'email', 'telefone_number', 'ticket']