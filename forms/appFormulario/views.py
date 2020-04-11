from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoForm
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
