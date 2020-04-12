from django.urls import path
from . import views

urlpatterns=[
    path('registro/',views.show_form, name='registro'),
    path('registrar/',views.post_form, name='registrar'),
    path('empleado/',views.show_empleado_form, name='empleado_form'),
    path('post_empleado',views.post_empleado_form, name='post_empleado_form'),
    path('registro_tickets/',views.show_tickets, name='registro_tickets'),
    path('registrar_tickets/',views.post_tickets, name='registrar_tickets'),
]
