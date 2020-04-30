from deusto11_nexus_components.models import EmployerLoginModel

class Authentication():

    def __init__(self):
        self.employer_exist = False

    def check_model_employer_authentication(self, model, logger, views_manager_service):
        context_exployers = views_manager_service.return_all_employer_context()
        login = False
        for employer in context_exployers["employers"]:
            if(employer.user_nick == model.user_nick and employer.password == model.password):
                login = True
        if(login):
            self.employer_exist = True
            logger.info_log(f"Exist nick {model.user_nick} with similar password {model.password}")
            return login
        else:
            logger.error_log(f"Nick or password not exist or coincidence with object in db")
            return login

    # Borrar metodo, no recorre el context y ademas ya se encarga el forms de no repetir atributos
    def user_nick_already_exist(self, registry_nick, logger, views_manager_service):
        context_exployers = views_manager_service.return_all_employer_context()
        for employer in context_exployers["employers"]:
            if(employer.user_nick == registry_nick):
                logger.error_log(f"The user {registry_nick} already exist, try other user")
                return True
            else:
                logger.info_log(f"Nick {registry_nick} not exist before")
                return False
