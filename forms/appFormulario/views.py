from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoForm,TicketsForm
# Create your views here.
def show_form(request):
    return render(request,'empleado_nexus.html')

def post_form(request):
    nombre=request.POST["nombre"]
    apellidos=request.POST["apellidos"]
    dni=request.POST["dni"]
    telefono=request.POST["telefono"]
    email=request.POST["email"]
    return HttpResponse(f"El usuario es {nombre}, los apellidos {apellidos}, su dni es {dni}  y el email es {email} y su telefono es {telefono}")

def show_empleado_form(request):
    form=EmpleadoForm()
    return render(request,'empleado_form.html', {'form':form})
    
def post_empleado_form(request):
    form=EmpleadoForm(request.POST)
    if form.is_valid(): 
        nombre=form.cleaned_data['nombre']
        apellidos=form.cleaned_data['apellidos']
        dni=form.cleaned_data['dni']
        telefono=form.cleaned_data['telefono']
        email=form.cleaned_data['email']
        return HttpResponse(f"El empleado es {nombre}, los apellidos {apellidos}, su dni es {dni} , su telefono es {telefono} y el email {email}")


def show_tickets(request):
    return render(request,'tickets_nexus.html')

def post_tickets(request):
    referencia=request.POST["referencia"]
    titulo=request.POST["titulo"]
    descripcion=request.POST["descripcion"]
    fechaapertura=request.POST["fechaapertura"]
    horaapertura=request.POST["horaapertura"]
    fecharesolucion=request.POST["fecharesolucion"]
    horaresolucion=request.POST["horaresolucion"]
    urgencia=request.POST["urgencia"]
    tipo=request.POST["tipo"]
    estado=request.POST["estado"]
    comentario=request.POST["comentario"]
    return HttpResponse(f"La referencia del ticket es {referencia}, su titulo es {titulo}, su descripcion es {descripcion}, su fecha de apertura es {fechaapertura} y su hora de apertura es {horaapertura}, su fecha de resolucion es {fecharesolucion} y su hora de resolucion es {horaresolucion},su urgencia es {urgencia}, el tipo de ticket es {tipo}, el estado del tickets es {estado} y los comentarios puestps son {comentario} ")

def show_tickets_form(request):
    form=TicketsForm()
    return render(request,'tickets_form.html', {'form':form})

def post_tickets_form(request):
    form=TicketsForm(request.POST)
    if form.is_valid(): 
        referencia=form.cleaned_data['referencia']
        titulo=form.cleaned_data['titulo']
        descripcion=form.cleaned_data['descripcion']
        fechaapertura=form.cleaned_data['fechaapertura']
        horaapertura=form.cleaned_data['horaapertura']
        fecharesolucion=form.cleaned_data['fecharesolucion']
        horaresolucion=form.cleaned_data['horaresolucion']
        urgencia=form.cleaned_data['urgencia']
        tipo=form.cleaned_data['tipo']
        estado=form.cleaned_data['estado']
        comentario=form.cleaned_data['comentario']
        return HttpResponse(f"La referencia del ticket es {referencia}, su titulo es {titulo}, su descripcion es {descripcion}, su fecha de apertura es {fechaapertura} y su hora de apertura es {horaapertura}, su fecha de resolucion es {fecharesolucion} y su hora de resolucion es {horaresolucion},su urgencia es {urgencia}, el tipo de ticket es {tipo}, el estado del tickets es {estado} y los comentarios puestps son {comentario} ")
