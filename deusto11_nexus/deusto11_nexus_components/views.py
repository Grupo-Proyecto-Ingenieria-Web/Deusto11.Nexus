from django.http import HttpResponse
from django.shortcuts import render
import deusto11_nexus_services as nexus_services

# _temaplateViews = nexus_services.TemplatesViews(request)

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Empleado(request):
    return render(request, 'empleado.html')

def Tickets(request):
    return render(request, 'tickets.html')

def Vlog(request):
    return render(request, 'vlog.html')
