import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json

class LoginPage (BasePage):

    def get_login(self):
        with open('./Assets/data/login_data/logininfo.json','r',encoding='utf8') as jdata:
            logindata = json.load(jdata)
            return logindata

    def type_in(self, by, value, text):
        self.type(by, value, text)
