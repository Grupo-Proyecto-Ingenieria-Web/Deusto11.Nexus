from django.urls import path
from . import views
from .common import statics

import deusto11_nexus_services.logging as nexus_services_logs
_logger = nexus_services_logs.Logging(statics.NEXUS_URLS_LOGGING_NAME)

try:
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index_default_view'),
        path('ticketPortal/', views.TicketPortalView.as_view(), name='ticket_default_portal'),
        path('employerPortal/', views.EmployerPortalView.as_view(), name='employer_default_portal'),
        path('vlogPortal/', views.VlogPortalView.as_view(), name='vlog_default_portal'),
        path('menuPortal/', views.MenuPortalView.as_view(), name='menu_default_portal'),
        path('employerPortal/create/', views.EmployerRegistryView.as_view(), name='employer_create'),
        path('employerPortal/update/<int:pk>/', views.UpdateEmployerProfileView.as_view(), name='employer_update'),
        path('machine/registry/', views.MachineRegistryView.as_view(), name='machine_registry'),
        path('machine/update/<int:pk>/', views.UpdateMachiView.as_view(), name='update_machine'),
        # path('ticket/registry/', views.TicketRegistryView.as_view(), name='ticket_registry'),
        path('ticket/update/<int:pk>/', views.UpdateTicketView.as_view(), name='update_ticket'),
        path('employer/emails/', views.EmailView.as_view(), name='employer_emails'),
        path('apiallemployer/',views.ApiAllEmployer.as_view(),name='api_all_employer'),
        path('apiallmachine/',views.ApiAllMachine.as_view(),name='api_all_machine'),
        path('apialltickets/',views.ApiAllTickets.as_view(),name='api_all_tickets'),
        path('apiallemails/',views.ApiAllEmail.as_view(),name='api_all_email'),       
        path('error/',views.ErrorView.as_view(),name='error_view'),
    ]      
except AttributeError:
    _logger.error_log("Atribute error exception, some url don't exist or it is not defined")
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index_default_view'),
    ] 