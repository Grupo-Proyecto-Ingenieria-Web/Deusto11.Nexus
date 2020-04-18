from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.views.generic import DetailView
# import deusto11_nexus_services as nexus_services
# from django.views.generic.edit import UpdateView, DeleteView

# _temaplateViews = nexus_services.TemplatesViews(request)

# Aqui falta logica de codigo para que una vez que haya login se redireccione a EmployerPortalView
class IndexView(View):

    tittle = 'Index nexus'
    
    def get(self, request, *args, **kwargs):
        form = EmployerLoginForm()
        context = {
            'tittle': tittle,
            'form': form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = EmployerLoginForm(request.POST)
        if form.is_valid():

            # form.save()
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
        context = {
            'tittle': tittle,
            'form': form
        }
        return render(request, 'employerRegistry.html', context)

    def post(self, request, *args, **kwargs):
        form = EmployerForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('employerRegistry')


class TicketRegistryView(View):

class MachineRegistryView(View):
        
# Todavia no hacer
# class UpdateEmployerProfileView(View):

# Todavia no hacer
# class UpdateMachiView(View):

# Todavia no hacer
# class UpdateTicketView(View):

# class NexusPortalView(DetailView):