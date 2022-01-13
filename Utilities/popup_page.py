import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json
class PopupPage(BasePage):

    def load_general_data(self):
        with open('./Assets/data/general_data/general_data.json','r',encoding='utf8') as jsondata:
            generaldata = json.load(jsondata)
        return generaldata
    
    def get_exist(self, by, value):
        return self.get_element_exist(by, value)
    
    def find_target_element(self, by, value):
        return self.find_element(by, value)
    
    def execute_target_script(self, scripts):
        # general_data = self.load_general_data()
        return self.execute_script(scripts)
    
    def get_text(self, by, value):
        return self.get_element_text(by, value)

    def click(self):
        self.click()
    
    def find_target_elements(self, by, value):
        return self.find_elements(by, value)