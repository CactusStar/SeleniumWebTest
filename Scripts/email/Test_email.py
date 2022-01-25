import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
from Objects.email_objects import EmailObjects
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
import time
from framework.BaseBrowser import BrowserEngine

class Testemail(unittest.TestCase):
    data_path = './Assets/data/email_data/email_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_labelselect(self):
        common_action = CommonOperation(self.driver)
        none_radio = common_action.find_element(EmailObjects.None_radio[0], EmailObjects.None_radio[1])
        none_selected = none_radio.is_selected()
        self.assertTrue(none_selected)
        daily_radio = common_action.find_element(EmailObjects.Daily_radio[0], EmailObjects.Daily_radio[1])
        daily_radio.click()
        daily_selected = daily_radio.is_selected()
        self.assertTrue(daily_selected)
        none_checked = none_radio.get_attribute("checked")
        self.assertIsNone(none_checked)
        

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testemail("test_labelselect"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)