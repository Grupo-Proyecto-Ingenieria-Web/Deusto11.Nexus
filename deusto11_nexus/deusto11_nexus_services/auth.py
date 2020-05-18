from deusto11_nexus_components.models import EmployerLoginModel

class Authentication():

    def __init__(self):
        self.employer_exist = False
        self.employer

    def check_model_employer_authentication(self, model, logger, views_manager_service):
        context_exployers = views_manager_service.return_all_employer_context()
        login = False
        for employer in context_exployers["employers"]:
            if(employer.user_nick == model.user_nick and employer.password == model.password):
                login = True
                self.employer = employer
        if(login):
            self.employer_exist = True
            logger.info_log(f"Exist nick {model.user_nick} with similar password {model.password}")
            return login
        else:
            logger.error_log(f"Nick or password not exist or coincidence with object in db")
            return login