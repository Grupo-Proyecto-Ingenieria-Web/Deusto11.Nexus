

class ViewsManagerService():

    def validate_form(self, form, logger):
        if (form.is_valid()):
            logger.info_log("Correct form structure")
            return True
        else:
            logger.error_log("Form not valid")
            return False

    def save_form(self, form, logger):
        if(form.save()):
            logger.info_log("Changes correctly input in database")
        else:
            logger.error_log("Changes not saved in database")

    def build_context_form(self, tittle, form):
        context = {
            'tittle': tittle,
            'form': form
        }
        return context

    def build_context_queryset_employers(self, queryset):
        context = {
            'employers': queryset
        }
        return context