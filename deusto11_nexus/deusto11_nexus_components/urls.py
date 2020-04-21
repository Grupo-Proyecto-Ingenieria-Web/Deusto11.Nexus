from django.urls import path
from django.contrib.auth.views import login, logout_then_login
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_default_view'),
    #para logearse
    path('',login,{'template_name': 'index.html'}.name='login'),
    #para salirte 
    #path('logout/',logout_then_login,name='logout'),
    path('employerPortal/', views.EmployerPortalView.as_view(), name='employer_default_portal'),
    path('employerPortal/create/', views.EmployerRegistryView.as_view(), name='employer_create'),
    path('employerPortal/update/<int:pk>/', views.UpdateEmployerProfileView.as_view(), name='employer_update'),
    path('machine/registry/', views.MachineRegistryView.as_view(), name='machine_registry'),
    # path('machine/update/<int:pk>/', views.UpdateMachiView.as_view(), name='update_machine'),
    path('ticket/registry/', views.TicketRegistryView.as_view(), name='ticket_registry'),
    # path('ticket/update/<int:pk>/', views.UpdateTicketView.as_view(), name='update_ticket'),
    
]