from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.views.generic import DetailView, ListView, UpdateView
from django.views import View
import logging
import deusto11_nexus_services.logging as nexus_services_logs
import deusto11_nexus_services.viewsManageService as nexus_services_views_manager
from .common import statics
# _temaplateViews = nexus_services.TemplatesViews(request)

_logger = nexus_services_logs.Logging(statics.NEXUS_VIEWS_LOGGING_NAME)
_views_manager_service = nexus_services_views_manager.ViewsManagerService()

class IndexView(View):

    def get(self, request, *args, **kwargs):  
        tittle = "Index nexus"
        form = EmployerLoginForm()
        _logger.info_log("Using EmployerLoginForm to create form in index")

        return render(request, 'index.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerLoginForm(request.POST)
        _views_manager_service.validate_and_save_form(form, _logger)

        return redirect('employerPortal')

class EmployerPortalView(ListView):

    model = Ticket
    template_name = "employerPortal.html"
    queryset_all_articles = Ticket.objects.order_by("id") 
    context_object_name = "list_employers_already_exists"  

    def get_context_data(self, **kwargs):
        all_context = super(EmployerPortalView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Principle employer portal"

        return all_context
   
class EmployerRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Employer registry page'
        form = EmployerForm()
        
        return render(request, 'employerRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        _views_manager_service.validate_and_save_form(form, _logger)

        return redirect('employerRegistry')


class TicketRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Tickets registry page'
        form = TicketForm()
        
        return render(request, 'ticketRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        _views_manager_service.validate_and_save_form(form, _logger)

        return redirect('ticketRegistry')

class MachineRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Machine registry page'
        form = MachineForm()
        
        return render(request, 'machineRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = MachineForm(request.POST)
        _views_manager_service.validate_and_save_form(form, _logger)

        return redirect('machineRegistry')
        
# Todavia no hacer
class UpdateEmployerProfileView(UpdateView):
    tittle = 'Machine registry page'
   

# Todavia no hacer
# class UpdateMachiView(View):

# Todavia no hacer
# class UpdateTicketView(View):

# class NexusPortalView(DetailView):

