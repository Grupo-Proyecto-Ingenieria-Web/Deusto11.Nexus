from django.contrib import admin
from .models import Employee, Ticket, Machine

# username and pass: nexus_admin

admin.site.register(Employee)
admin.site.register(Ticket)
admin.site.register(Machine)