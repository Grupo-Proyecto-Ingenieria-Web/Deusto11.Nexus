from django import forms
from .models import Employee, Ticket, Machine

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

