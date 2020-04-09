from django.contrib import admin
from .models import Empleado, Tickets, Equipo

# username and pass: nexus_admin

admin.site.register(Empleado)
admin.site.register(Tickets)
admin.site.register(Equipo)

# Register your models here.
