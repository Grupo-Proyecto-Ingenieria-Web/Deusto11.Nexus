# from deusto11_nexus_components.models import Employee

class Authentication():

    def __init__(self):
        self.employer_exist = False

    def check_model_employer_authentication(self, model, logger, views_manager_service):
        # queryset_all_employers = Employee.objects.order_by("id")
        context_exployers = views_manager_service.return_all_employer_context(views_manager_service)
        for employer in context_exployers["employers"]:
            if(employer.user_nick == model.user_nick and employer.password == model.password):
                self.employer_exist = True
                logger.info_log("Exist nick with similar password")
                return True
            else:
                logger.error_log("Nick or password not exist or coincidence with object in db")
                return False

    def user_nick_already_exist(self, registry_nick, logger, views_manager_service):
        context_exployers = views_manager_service.return_all_employer_context(views_manager_service)
        for employer in context_exployers["employers"]:
            if(employer.user_nick == registry_nick):
                logger.error_log(f"The user {registry_nick} already exist, try other user")
                return True
            else:
                logger.info_log(f"Nick {registry_nick} not exist before")
                return False

