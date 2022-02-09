import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
import time
from Objects.portal_objects import PortalObjects
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
from framework.BaseBrowser import BrowserEngine

class Testportal(unittest.TestCase):
    data_path = './Assets/data/portal_data/portal_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_animate(self):
        common_action = CommonOperation(self.driver)
        otherlines = common_action.find_target_elements(PortalObjects.Otherlines_input[0], PortalObjects.Otherlines_input[1])
        loopcount = len(otherlines)
        for i in range(0, loopcount):
            if i == 0:
                continue
            self.assertEqual(otherlines[i].value_of_css_property("visibility"), self.data["VisiblityAttribute"]["item0"])
        target = common_action.find_target_element(PortalObjects.Firstline_input[0], PortalObjects.Firstline_input[1])
        common_action.move_mousescroll(target)
        time.sleep(3)
        
        for i in range(0, loopcount):
            if i == 0:
                continue
            self.assertEqual(otherlines[i].value_of_css_property("visibility"), self.data["VisiblityAttribute"]["item1"])
        

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testportal("test_animate"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)