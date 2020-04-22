from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.views.generic import DetailView, ListView, UpdateView
from django.views import View
import logging
import deusto11_nexus_services as nexus_services

# _temaplateViews = nexus_services.TemplatesViews(request)

# Esto se pasara a nexus_services en un futuro
class ViewsManagerService():

    def validate_and_save_form(self, form):
        if form.is_valid():
            _logger.info("Correct form structure")
            if(form.save()):
                _logger.info("Changes correctly input in database")
            else:
                _logger.error("Cahanges not saved in database")


    def build_context_form(self, tittle, form):
        context = {
            'tittle': tittle,
            'form': form
        }
        return context

_logger = logging.getLogger("nexus.componenets.views")
_viewsManagerService = ViewsManagerService()

# Aqui falta logica de codigo para que una vez que haya login se redireccione a EmployerPortalView
class IndexView(View):

    def get(self, request, *args, **kwargs):  
        tittle = 'Index nexus'
        form = EmployerLoginForm()
        _logger.info("Unsing EmployerLoginForm to create form in index")

        return render(request, 'index.html', _viewsManagerService.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerLoginForm(request.POST)
        _viewsManagerService.validate_and_save_form(form)

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
   
# employerRegistry.html debe tener un <a href="{% url 'employerPortal' %}">Volver a la lista</a> para volver al portal de employee
class EmployerRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Employer registry page'
        form = EmployerForm()
        
        return render(request, 'employerRegistry.html', _viewsManagerService.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        _viewsManagerService.validate_and_save_form(form)

        return redirect('employerRegistry')


class TicketRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Tickets registry page'
        form = TicketForm()
        
        return render(request, 'ticketRegistry.html', _viewsManagerService.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        _viewsManagerService.validate_and_save_form(form)

        return redirect('ticketRegistry')

class MachineRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        tittle = 'Machine registry page'
        form = MachineForm()
        
        return render(request, 'machineRegistry.html', _viewsManagerService.build_context_form(tittle, form))

    def post(self, request, *args, **kwargs):
        form = MachineForm(request.POST)
        _viewsManagerService.validate_and_save_form(form)

        return redirect('machineRegistry')
        
# Todavia no hacer
class UpdateEmployerProfileView(UpdateView):
    #tittle = 'Machine registry page'
    model=Employee
    #fields=[]
    form_class=EmployerForm
    template_name="nexus/UpdateEmployerProfile.html"
   

# Todavia no hacer
 class UpdateMachiView(UpdateView):
    model=Machine
    #fields=[]
    form_class=MachineForm
    template_name="nexus/UpdateMachine.html"

# Todavia no hacer
 class UpdateTicketView(UpdateView):
    model=Ticket
    #fields=[]
    form_class=TicketForm
    template_name="nexus/UpdateTicket.html"

 class NexusPortalView(DetailView):

