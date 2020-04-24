from deusto11_nexus_components.common import Employee

class Authentication():

    def __init__(self):
        self.employer_exist = False

    def check_model_employer_authentication(self, model, logger):
        queryset_all_employers = Employee.object.order_by("id") 
        for employer in queryset_all_employers:
            if(employer.user_nick == model.user_nick and employer.password == model.password):
                self.employer_exist = True
                logger.info_log("Exist nick with similar password")
                return True
            else:
                logger.error_log("Nick or password not exist or coincidence with object in db")
                return False

    def check_if_user_nick_already_exist(self):
        return False