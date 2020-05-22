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
            'password' : forms.PasswordInput()
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
            'starting_date' : DateInput(),
            'resolution_date' : DateInput(),
            'comment' : forms.Textarea()
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
        
class EmployerLoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['dni', 'name', 'surname', 'email', 'telefone_number', 'ticket']
        

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"