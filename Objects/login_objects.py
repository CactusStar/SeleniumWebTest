import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage


class LoginObjects (BasePage):
    
    Username = ["id", 'login_field']
    Password = ["id", 'password']
    Signin = ["name", 'commit']
    IncorrectInfo = ["css", ".container-lg.px-2"]