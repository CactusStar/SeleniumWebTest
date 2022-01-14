import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json
class PopupPage(BasePage):

    def load_general_data(self):
        with open('./Assets/data/general_data/general_data.json','r',encoding='utf8') as jsondata:
            generaldata = json.load(jsondata)
        return generaldata

    def click(self):
        self.click()