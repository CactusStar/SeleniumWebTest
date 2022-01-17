import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json

class NewRepoPage(BasePage):

    def load_newrepo_data(self):
        with open('./Assets/data/newrepo_data/newrepo_data.json','r',encoding='utf8') as jsondata:
            newrepodata = json.load(jsondata)
        return newrepodata