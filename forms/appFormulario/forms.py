from django import forms
class EmpleadoForm(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=100)
    apellidos=forms.CharField(label="Apellidos", max_length=150)
    dni=forms.CharField(label="Dni")
    telefono=forms.IntegerField(label="Telefono")
    email=forms.EmailField(label="Email", required=False)
    
    

