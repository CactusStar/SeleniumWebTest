import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json

class IssuesPage(BasePage):

    def load_issues_data(self):
        with open('./Assets/data/issues_data/issues_data.json','r',encoding='utf8') as jsondata:
            issuedata = json.load(jsondata)
        return issuedata
    
