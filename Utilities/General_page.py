import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json
class GeneralPage(BasePage):

    def load_general_data(self):
        with open('./Assets/data/general_data/general_data.json','r',encoding='utf8') as jsondata:
            generaldata = json.load(jsondata)
        return generaldata
    
    def execute_target_script(self, scripts):
        # general_data = self.load_general_data()
        return self.execute_script(scripts)

