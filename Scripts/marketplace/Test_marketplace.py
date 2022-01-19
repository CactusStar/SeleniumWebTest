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
    
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    
    def test_treeitems(self):
        marketplace_page = MarketplacePage(self.driver)
        common_actions = CommonOperation(self.driver)
        data = marketplace_page.load_marketplace_data()
        list = common_actions.find_elements(MarketplaceObjects.Type_list[0], MarketplaceObjects.Type_list[1])
        loopcount = len(list)
        for i in range (0, loopcount):
            self.assertEqual(data["Typelist"]["item" + str(i)], list[i].text)

    def test_free(self):
        marketplace_page = MarketplacePage(self.driver)
        common_actions = CommonOperation(self.driver)
        data = marketplace_page.load_marketplace_data()
        explore_free = common_actions.find_element(MarketplaceObjects.Free_link[0], MarketplaceObjects.Free_link[1])
        explore_free.click()
        free_link = common_actions.get_current_url()
        self.assertEqual(data["Freelink"], free_link)
        close_link = common_actions.find_element(MarketplaceObjects.Closefree_link[0], MarketplaceObjects.Closefree_link[1])
        close_link.click()
        market_link = common_actions.get_current_url()
        self.assertEqual(data["marketlink"], market_link)

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