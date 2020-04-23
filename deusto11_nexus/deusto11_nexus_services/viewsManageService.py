

class ViewsManagerService():

    def validate_and_save_form(self, form, logger):
        if (form.is_valid()):
            logger.info_log("Correct form structure")
            if(form.save()):
                logger.info_log("Changes correctly input in database")
            else:
                logger.error_log("Cahanges not saved in database")


    def build_context_form(self, tittle, form):
        context = {
            'tittle': tittle,
            'form': form
        }
        return context