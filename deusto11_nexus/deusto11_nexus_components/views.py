from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.views.generic import DetailView
import logging
# import deusto11_nexus_services as nexus_services
# from django.views.generic.edit import UpdateView, DeleteView

# _temaplateViews = nexus_services.TemplatesViews(request)

_logger = logging.getLogger("nexus.componenets.views")
_viewsMethosManager = ViewsMethodsManager

# Aqui falta logica de codigo para que una vez que haya login se redireccione a EmployerPortalView
class IndexView(View):

    tittle = 'Index nexus'
    

    def get(self, request, *args, **kwargs):
        form = EmployerLoginForm()
        _logger.info("Unsing EmployerLoginForm to create form in index")
        
        return render(request, 'index.html', _viewsMethosManager.build_context(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerLoginForm(request.POST)
        _viewsMethosManager.validate_and_save_form(form)

        return redirect('employerPortal')
        # form = EmployerLoginForm()
        # context = {
            # 'tittle': tittle,
        # 'form': form
        # }
        # return render(request, 'index.html', context)

class EmployerPortalView(ListView):

    model = Ticket
    template_name = "employerPortal.html"
    querysetAllArticles = Ticket.objects.order_by("id") 
    context_object_name = "list_employers_already_exists"  

    def get_context_data(self, **kwargs):
        all_context = super(EmployerPortalView, self).get_context_data(**kwargs) 
        all_context["tittle"] = "Principle employer portal"

        return all_context
   
# employerRegistry.html debe tener un <a href="{% url 'employerPortal' %}">Volver a la lista</a> para volver al portal de employee
class EmployerRegistryView(View):

    tittle = 'Employer registry page'
    
    def get(self, request, *args, **kwargs):
        form = EmployerForm()
        
        return render(request, 'employerRegistry.html', _viewsMethosManager.build_context(tittle, form))

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        _viewsMethosManager.validate_and_save_form(form)

        return redirect('employerRegistry')


class TicketRegistryView(View):

    tittle = 'Tickets registry page'
    
    def get(self, request, *args, **kwargs):
        form = TicketForm()
        
        return render(request, 'ticketRegistry.html', _viewsMethosManager.build_context(tittle, form))

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        _viewsMethosManager.validate_and_save_form(form)

        return redirect('ticketRegistry')

class MachineRegistryView(View):

    tittle = 'Machine registry page'
    
    def get(self, request, *args, **kwargs):
        form = MachineForm()
        
        return render(request, 'machineRegistry.html', _viewsMethosManager.build_context(tittle, form))

    def post(self, request, *args, **kwargs):
        form = MachineForm(request.POST)
        _viewsMethosManager.validate_and_save_form(form)

        return redirect('machineRegistry')
        
# Todavia no hacer
# class UpdateEmployerProfileView(View):

# Todavia no hacer
# class UpdateMachiView(View):

# Todavia no hacer
# class UpdateTicketView(View):

# class NexusPortalView(DetailView):

# Esto se pasara a nexus_services en un futuro
class ViewsMethodsManager():

    def validate_and_save_form(self, form):
        if form.is_valid():
            _logger.info("Correct form structure")
            if(form.save()):
                _logger.info("Changes correctly input in database")
            else:
                _logger.error("Cahanges not saved in db")

    def build_context(self, tittle, form):
        context = {
            'tittle': tittle,
            'form': form
        }
        return context