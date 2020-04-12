from django import forms
class EmpleadoForm(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=100)
    apellidos=forms.CharField(label="Apellidos", max_length=150)
    dni=forms.CharField(label="Dni")
    telefono=forms.IntegerField(label="Telefono")
    email=forms.EmailField(label="Email", required=False)

class TicketsForm(forms.Form):
    referencia=forms.IntegerField(label="Referencia")
    titulo=forms.CharField(label="Titulo", max_length=100)
    descripcion=forms.CharField(label="Descripcion", max_length=1000)
    fechaapertura=forms.DateField(label="FechaApertura")
    horaapertura=forms.DateTimeField(label="HoraApertura")
    fecharesolucion=forms.DateField(label="FechaResolucion")
    horaresolucion=forms.DateTimeField(label="HoraResolucion")
    nivelurgencia=forms.CharField(label="NivelUrgencia", max_length=40)
    estadoticket=forms.CharField(label="EstadoTicket", max_length=40)
    comentario=forms.CharField(label="Comentario", max_length=1000)
    

