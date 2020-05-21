from django.urls import (get_resolver, get_urlconf, resolve, 
                         reverse, NoReverseMatch)
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Employee, Ticket, Machine, EmployerLoginModel
from .forms import EmployerForm, TicketForm, MachineForm, EmployerLoginForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views import View
from .common import statics
from django.forms.models import model_to_dict
from django.template.base import TemplateSyntaxError
from django.template import TemplateDoesNotExist

import deusto11_nexus_services.logging as nexus_services_logs
import deusto11_nexus_services.viewsManageService as nexus_services_views_manager
import deusto11_nexus_services.auth as nexus_services_auth

""" Instances  of nexus_components module """
_logger = nexus_services_logs.Logging(statics.NEXUS_VIEWS_LOGGING_NAME)
_views_manager_service = nexus_services_views_manager.ViewsManagerService()
_auth = nexus_services_auth.Authentication()

""" Index default view class methods, here the user can login or redirect to register page """
class IndexView(View):

    def get(self, request, *args, **kwargs): 
        try: 
            tittle = "Index nexus"
            form = EmployerLoginForm()
            _logger.info_log("Using EmployerLoginForm to create form in index")
            return render(request, 'index.html', _views_manager_service.build_context_form(tittle, form))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

    def post(self, request, *args, **kwargs):
        try:
            form = EmployerLoginForm(request.POST)
            login_model = self.__create_model(request)
 
            if(_auth.check_model_employer_authentication(login_model, _logger, _views_manager_service)):
                return redirect(statics.MENU_DEFAULT_PORTAL_URL)
            else:
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)


    def __create_model(self, request):
        login_model = EmployerLoginModel()
        login_model.user_nick = request.POST.get("user_nick")
        login_model.password = request.POST.get("password")
        return login_model

""" Ticket list view methos & delete tickets by post mothod """
class TicketPortalView(View):

    def get(self, request, *args, **kwargs):
        try:
            tittle = "Principle employer portal"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'ticketPortal.html', _views_manager_service.build_context_employer_portal(tittle))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)
    
  
    def post(self, request, *args, **kwargs):
        try:
            id_object = request.POST.get('Delete')
            delete_ticket = Ticket.objects.filter(id = id_object)
            if(delete_ticket.delete()):
                _logger.info_log("object delete succesfully")
            else:
                _logger.error_log("the object not deleted or error")
            return redirect(statics.TICKET_DEFAULT_PORTAL_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)


class EmployerPortalView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = "Principle employer portal"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'employerPortal.html', _views_manager_service.build_context_machines_portal(tittle, _auth.employer))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)
    
  
    def post(self, request, *args, **kwargs):
        try:
            id_object = request.POST.get('Delete')
            delete_employer = Machine.objects.filter(id = id_object)
            if(delete_employer.delete()):
                _logger.info_log("object delete succesfully")
            else:
                _logger.error_log("the object not deleted or error")
            return redirect(statics.MACHINE_DEFAULT_PORTAL_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)
    
class EmailView(View):
    def get(self, request, *args, **kwargs):
        try:
            tittle = "Principle employer portal"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'emailPortal.html', _views_manager_service.build_context_employer_portal(tittle))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)
  
    def post(self, request, *args, **kwargs):
        try:
            id_object = request.POST.get('Delete')
            delete_ticket = Ticket.objects.filter(id = id_object)
            if(delete_ticket.delete()):
                _logger.info_log("object delete succesfully")
            else:
                _logger.error_log("the object not deleted or error")
            return redirect(statics.TICKET_DEFAULT_PORTAL_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)


""" Menu class to get vlog page of the  """
class MenuPortalView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Menu  nexus'
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'menu.html', _views_manager_service.build_context_form(tittle, ""))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

""" Vlog class to get vlog page of the """
class VlogPortalView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Vlog nexus'
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'vlogPortal.html', _views_manager_service.build_context_form(tittle, ""))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

""" Error class to get error page if there are some exceptions """
class ErrorView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Error template'
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return render(request, 'templateError.html', _views_manager_service.build_context_form(tittle, ""))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)
   
""" Default employer registry page view """
class EmployerRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Employer registry page'
            form = EmployerForm()
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:        
                return render(request, 'employerRegistry.html', _views_manager_service.build_context_form(tittle, form))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

    def post(self, request, *args, **kwargs):
        try:
            form = EmployerForm(request.POST)
            registry_user = request.POST.get("user_nick")
            if(_views_manager_service.validate_form(form, _logger)):
                _views_manager_service.save_form(form, _logger)
                return redirect(statics.TICKET_DEFAULT_PORTAL_URL)
            else:
                return redirect(statics.EMPLOYER_CREATE_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)

""" Default employer registry page view  """
class TicketRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Tickets registry page'
            form = TicketForm()
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:        
                return render(request, 'ticketRegistry.html', _views_manager_service.build_context_form(tittle, form))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

    def post(self, request, *args, **kwargs):
        try:
            form = TicketForm(request.POST)
            if(_views_manager_service.validate_form(form, _logger)):
                _views_manager_service.save_form(form, _logger)
                return redirect(statics.TICKET_DEFAULT_PORTAL_URL)
            else:
                return redirect(statics.TICKET_REGISTRY_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)

    def __create_ticket_model(self, request):
        ticket_model = Ticket()
        ticket_model.reference_number = request.POST.get["reference_number"]
        # ticket_model.


""" Default machine registry page view """
class MachineRegistryView(View):
    
    def get(self, request, *args, **kwargs):
        try:
            tittle = 'Machine registry page'
            form = MachineForm()
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:      
                return render(request, 'machineRegistry.html', _views_manager_service.build_context_form(tittle, form))
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

    def post(self, request, *args, **kwargs):
        try:
            form = MachineForm(request.POST)
            if(_views_manager_service.validate_form(form, _logger)):
                _views_manager_service.save_form(form, _logger)
                return redirect(statics.TICKET_DEFAULT_PORTAL_URL)
            else:
                return redirect(statics.MACHINE_REGISTRY_URL)
        except (NoReverseMatch):
            _logger.error_log(statics.NO_REVERSE_MATCH_MESSAGE)
            return redirect(statics.ERROR_URL)
        
""" Default employer update page view  """
class UpdateEmployerProfileView(UpdateView):

    model = Employee
    form_class = EmployerForm
    template_name = "updateEmployerProfile.html"
    success_url = reverse_lazy(statics.TICKET_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        try:
            all_context = super( UpdateEmployerProfileView, self).get_context_data(**kwargs) 
            all_context["tittle"] = "Employer registry page"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return all_context
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)
    
""" Default machine update page view """
class UpdateMachiView(UpdateView):
    model=Machine
    form_class=MachineForm
    template_name="UpdateMachine.html"
    success_url= reverse_lazy(statics.TICKET_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        try:
            all_context = super( UpdateMachiView, self).get_context_data(**kwargs) 
            all_context["tittle"] = "Machine registry page"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return all_context
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

""" Default ticket update page view """
class UpdateTicketView(UpdateView):

    model = Ticket
    form_class = TicketForm
    template_name = "UpdateTicket.html"
    success_url = reverse_lazy(statics.TICKET_DEFAULT_PORTAL_URL)

    def get_context_data(self, **kwargs):   
        try:
            all_context = super(UpdateTicketView, self).get_context_data(**kwargs) 
            all_context["tittle"] = "Ticket registry page"
            if (_auth.employer.dni == "12345678R"): # Default user_dni when did a new object
                return redirect(statics.INDEX_DEFAULT_VIEW_URL)
            else:
                return all_context
        except (TemplateDoesNotExist, TemplateSyntaxError, NoReverseMatch) :
            _logger.error_log(statics.TEMPLATE_DOES_NOT_EXIST)
            return redirect(statics.ERROR_URL)

class ApiAllEmployer(View):
    def get(self,request):
        #get metod
        dlist=Employee.objects.all()
        return JsonResponse(list(dlist.values()),safe=False)
    
    def post(self,request):
        #post metod
        employe=Employee()
        employe.dni=request.POST['dni']
        employe.email=request.POST['email']
        employe.name=request.POST['name']
        employe.password=request.POST['password']
        employe.surname=request.POST['surname']
        employe.telefone_number.POST['telefone_number']
        employe.ticket.POST['ticket']
        employe.user_nick.POST['user_nick']

    
class ApiAllMachine(View):
    def get(self,request):
        #get metod
        dlist=Machine.objects.all()
        return JsonResponse(list(dlist.values()),safe=False)
    
    def post(self,request):
        #post metod
        machine=Machine()
        machine.brand.POST['brand']
        machine.floor_on_premise.POST['floor_on_premise']
        machine.get_date.POST['get_date']
        machine.machine_type.POST['machine_type']
        machine.model.POST['model']
        machine.provider_name.POST['provider_name']
        machine.provider_telefone.POST['provider_telefone']
        machine.set_number.POST['set_number']
        machine.start_up_date.POST['start_up_date']
        

class ApiAllTickets(View):
    def get(self,request):
        #get metod
        dlist=Ticket.objects.all()
        return JsonResponse(list(dlist.values()),safe=False)
    
    def post(self,request):
        #post metod
        ticket=Ticket()
        ticket.comment.POST['comment']
        ticket.description.POST['description']
        ticket.machine.POST['machine']
        ticket.reference_number.POST['reference_number']
        ticket.resolution_date.POST['resolution_date']
        ticket.starting_date.POST['starting_date']
        ticket.status.POST['status']
        ticket.ticket_type.POST['ticket_type']
        ticket.title.POST['title']
        ticket.urgency_level.POST['urgency_level']

    

#This is to call only one objects

class ApiEmployer(View):
    def get(self,request,pk):
        #get metod
        dlist=Employee.objects.get(pk=pk)
        return JsonResponse(model_to_dict(dlist))
    
    #def post(self,request):
        #post metod

    #def put(self,request):
        #put metod

    #def delete(self,request):
        #delete metod


class ApiMachine(View):
    def get(self,request):
        #get metod
        dlist=Machine.objects.get(pk=pk)
        return JsonResponse(model_to_dict(dlist))
    
    #def post(self,request):
        #post metod

    #def put(self,request):
        #put metod

    #def delete(self,request):
        #delete metod


class ApiTickets(View):
    def get(self,request):
        #get metod
        dlist=Ticket.objects.get(pk=pk)
        return JsonResponse(model_to_dict(dlist))
    
    #def post(self,request):
        #post metod

    #def put(self,request):
        #put metod

    #def delete(self,request):
        #delete metod
