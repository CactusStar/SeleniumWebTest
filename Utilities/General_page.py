import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json
class GeneralPage(BasePage):
    
    def execute_target_script(self, scripts):
        # general_data = self.load_general_data()
        return self.execute_script(scripts)

