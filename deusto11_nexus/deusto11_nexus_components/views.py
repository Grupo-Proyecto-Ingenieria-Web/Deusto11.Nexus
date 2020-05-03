from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine, EmployerLoginModel
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views import View
from .common import statics
import deusto11_nexus_services.logging as nexus_services_logs
import deusto11_nexus_services.viewsManageService as nexus_services_views_manager
import deusto11_nexus_services.auth as nexus_services_auth

#Con esto hacemos los logins

_logger = nexus_services_logs.Logging(statics.NEXUS_VIEWS_LOGGING_NAME)
_views_manager_service = nexus_services_views_manager.ViewsManagerService()
_auth = nexus_services_auth.Authentication()

#Aqui tenemos las views de index
class IndexView(View):

    def get(self, request, *args, **kwargs):  
        tittle = "Index nexus"
        form = EmployerLoginForm()
        _logger.info_log("Using EmployerLoginForm to create form in index")
        return render(request, 'index.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerLoginForm(request.POST)
        login_model = self.__create_model(request)
        if(_auth.check_model_employer_authentication(login_model, _logger, _views_manager_service)):
            return redirect(statics.EMPLOYER_DEFAULT_PORTAL_URL, 2)
        else:
            return redirect(statics.INDEX_DEFAULT_VIEW_URL)

    def __create_model(self, request):
        login_model = EmployerLoginModel()
        login_model.user_nick = request.POST.get("user_nick")
        login_model.password = request.POST.get("password")
        return login_model

#La view de employer
class EmployerPortalView(View):

    def get(self, request, *args, **kwargs):
        tittle = "Principle employer portal"
        return render(request, 'employerPortal.html', _views_manager_service.build_context_employer_portal(tittle))

    # metodo delete basado en post
    def post(self, request, *args, **kwargs):
        id_object = request.POST.get('Delete')
        delete_ticket = Ticket.objects.filter(id = id_object)
        if(delete_ticket.delete()):
            _logger.info_log("object delete succesfully")
        else:
            _logger.error_log("the object not deleted or error")
        return redirect(statics.EMPLOYER_DEFAULT_PORTAL_URL)

#El vlog informativo
class VlogPortalView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Vlog nexus'
        return render(request, 'vlogPortal.html', _views_manager_service.build_context_form(tittle, ""))
   
# Falta comprobar que la nick sea siempre diferente
class EmployerRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Employer registry page'
        form = EmployerForm()        
        return render(request, 'employerRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        registry_user = request.POST.get("user_nick")
        if(_views_manager_service.validate_form(form, _logger)):
            _views_manager_service.save_form(form, _logger)
            return redirect('employer_default_portal')
        else:
            return redirect(statics.EMPLOYER_CREATE_URL)

#Para registrar un ticket
class TicketRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Tickets registry page'
        form = TicketForm()        
        return render(request, 'ticketRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        if(_views_manager_service.validate_form(form, _logger)):
            _views_manager_service.save_form(form, _logger)
            return redirect(statics.EMPLOYER_DEFAULT_PORTAL_URL)
        else:
            return redirect(statics.TICKET_REGISTRY_URL)

#Para registrar una maquina
class MachineRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Machine registry page'
        form = MachineForm()      
        return render(request, 'machineRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = MachineForm(request.POST)
        if(_views_manager_service.validate_form(form, _logger)):
            _views_manager_service.save_form(form, _logger)
            return redirect(statics.EMPLOYER_DEFAULT_PORTAL_URL)
        else:
            return redirect(statics.MACHINE_REGISTRY_URL)
        
# Todavia no hacer
#Actualizar el empleado
class UpdateEmployerProfileView(UpdateView):

    model = Employee
    form_class = EmployerForm
    template_name = "updateEmployerProfile.html"
    success_url = reverse_lazy(statics.EMPLOYER_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        all_context = super( UpdateEmployerProfileView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Employer registry page"
        return all_context
    

    
# Todavia no hacer
#Actualizar la maquina
class UpdateMachiView(UpdateView):
    model=Machine
    form_class=MachineForm
    template_name="UpdateMachine.html"
    success_url= reverse_lazy(statics.EMPLOYER_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        all_context = super( UpdateMachiView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Machine registry page"
        return all_context

# Todavia no hacer
#Actualizar el ticket
class UpdateTicketView(UpdateView):

    model = Ticket
    form_class = TicketForm
    template_name = "UpdateTicket.html"
    success_url = reverse_lazy(statics.EMPLOYER_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        all_context = super(UpdateTicketView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Ticket registry page"
        return all_context
