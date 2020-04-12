from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('empleado', views.Empleado, name='Empleado'),
    path('tickets', views.Tickets, name='Tickets'),
    path('vlog', views.Vlog, name='Vlog'),
    path('empleado/nuevoEmpleado', views.show_empleado_form, name='show_empleado_form'),
]