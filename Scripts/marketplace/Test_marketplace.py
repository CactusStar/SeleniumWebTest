import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
from Objects.marketplace_objects import MarketplaceObjects
from Utilities.Marketplace_page import MarketplacePage
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
import time
from framework.BaseBrowser import BrowserEngine

class TestMarketplace(unittest.TestCase):
    data_path = './Assets/data/marketplace_data/marketplace_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)
    
    def test_treeitems(self):
        common_actions = CommonOperation(self.driver)
        # data = common_actions.load_data(self.data_path)
        list = common_actions.find_elements(MarketplaceObjects.Type_list[0], MarketplaceObjects.Type_list[1])
        loopcount = len(list)
        for i in range (0, loopcount):
            self.assertEqual(self.data["Typelist"]["item" + str(i)], list[i].text)

    def test_free(self):
        common_actions = CommonOperation(self.driver)
        explore_free = common_actions.find_element(MarketplaceObjects.Free_link[0], MarketplaceObjects.Free_link[1])
        explore_free.click()
        free_link = common_actions.get_current_url()
        self.assertEqual(self.data["Freelink"], free_link)
        close_link = common_actions.find_element(MarketplaceObjects.Closefree_link[0], MarketplaceObjects.Closefree_link[1])
        close_link.click()
        market_link = common_actions.get_current_url()
        self.assertEqual(self.data["marketlink"], market_link)

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestMarketplace("test_treeitems"))
    suit.addTest(TestMarketplace("test_free"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)