from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine, EmployerLoginModel
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
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
            return redirect('employer_default_portal')
        else:
            return redirect('index_default_view')

    def __create_model(self, request):
        login_model = EmployerLoginModel()
        login_model.user_nick = request.POST.get("user_nick")
        login_model.password = request.POST.get("password")
        return login_model

#La view de employer
class EmployerPortalView(ListView):

    model = Ticket
    template_name = "employerPortal.html"
    queryset_all_articles = Ticket.objects.order_by("id") 
    context_object_name = "list_employers_already_exists"  

    def get_context_data(self, **kwargs):
        all_context = super(EmployerPortalView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Principle employer portal"
        return all_context
   
# Falta comprobar que la nick sea siempre diferente
#Para registrar un empleado
class EmployerRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Employer registry page'
        form = EmployerForm()        
        return render(request, 'employerRegistry.html', _views_manager_service.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        registry_user = request.POST.get("user_nick")
        if(_views_manager_service.validate_form(form, _logger) and not 
        _auth.user_nick_already_exist(registry_user, _logger, _views_manager_service)):
            _views_manager_service.save_form(form, _logger)
            return redirect('employer_default_portal')
        else:
            return redirect("employer_create")

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
            return redirect('employer_default_portal')
        else:
            return redirect("ticket_registry")

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
            return redirect('employer_default_portal')
        else:
            return redirect("machine_registry")
        
# Todavia no hacer
#Actualizar el empleado
class UpdateEmployerProfileView(UpdateView):
    #tittle = 'Machine registry page'
    model=Employee
    form_class=EmployerForm
    template_name="UpdateEmployerProfile.html"
    success_url= reverse_lazy('employer_update')
    

# Todavia no hacer
#Actualizar la maquina
class UpdateMachiView(UpdateView):
    model=Machine
    form_class=MachineForm
    template_name="UpdateMachine.html"
    success_url= reverse_lazy('update_machine')

# Todavia no hacer
#Actualizar el ticket
class UpdateTicketView(UpdateView):
    model=Ticket
    form_class=TicketForm
    template_name="UpdateTicket.html"
    success_url= reverse_lazy('update_ticket')

#class NexusPortalView(DetailView):

