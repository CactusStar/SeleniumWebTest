import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage
import json
class MarketplacePage(BasePage):

    def load_marketplace_data(self):
        with open('./Assets/data/marketplace_data/marketplace_data.json','r',encoding='utf8') as jsondata:
            marketplacedata = json.load(jsondata)
        return marketplacedata
