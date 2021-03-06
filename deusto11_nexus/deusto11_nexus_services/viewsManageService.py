from deusto11_nexus_components.models import Employee, Ticket, Machine, Email

class ViewsManagerService():

    def validate_form(self, form, logger):
        if (form.is_valid()):
            logger.info_log("Correct form structure")
            return True
        else:
            logger.error_log("Form not valid, default value or some value already exist in database")
            logger.warning_log("Here are the unique models fields: set_number, reference_number, dni, user_nick")
            return False

    def save_form(self, form, logger):
        if(form.save()):
            logger.info_log("Changes correctly input in database")
        else:
            logger.error_log("Changes not saved in database, something maybe already exist")

    def build_context_ticket_portal(self, title, logged_employer):
        queryset_tickets = Ticket.objects.order_by("id") 
        context = {
            'title': title,
            'list_tickets_already_exists': queryset_tickets,
            'logged_employer': logged_employer
        }
        return context

    def build_context_machines_portal(self, title, logged_employer):
        queryset_machines = Machine.objects.order_by("id")
        context = {
            'title': title,
            'list_machines_already_exists': queryset_machines,
            'logged_employer': logged_employer
        }
        return context

    def build_context_email_portal(self, title, logged_employer):
        queryset_emails = Email.objects.order_by("id")
        context = {
            'title': title,
            'list_machines_already_exists': queryset_emails,
            'logged_employer': logged_employer
        }
        return context


    def build_context_form(self, title, form):
        queryset_machines = Machine.objects.order_by("id")
        context = {
            'title': title,
            'list_machines_already_exists': queryset_machines,
            'form' : form
        }
        return context

    def build_context_queryset_employers(self, queryset):
        context = {
            'employers': queryset
        }
        return context

    def return_all_employer_context(self):
        queryset_all_employers = Employee.objects.order_by("id")    
        return self.build_context_queryset_employers(queryset_all_employers)