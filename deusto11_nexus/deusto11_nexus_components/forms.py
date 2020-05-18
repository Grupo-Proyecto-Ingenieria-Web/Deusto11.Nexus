from django import forms
from .models import Employee, Ticket, Machine, Email

""" All forms by ModelForm"""
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"
        
class EmployerLoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['dni', 'name', 'surname', 'email', 'telefone_number', 'ticket']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"