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

    def test_eachlabelContent(self):
        common_action = CommonOperation(self.driver)
        none_content = common_action.get_text(EmailObjects.None_content[0], EmailObjects.None_content[1])
        self.assertEqual(self.data["NoneContent"], none_content)
        daily_content = common_action.get_text(EmailObjects.Daily_content[0], EmailObjects.Daily_content[1])
        self.assertEqual(self.data["DailyContent"], daily_content)
        weekly_content = common_action.get_text(EmailObjects.Weekly_content[0], EmailObjects.Weekly_content[1])
        self.assertEqual(self.data["WeeklyContent"], weekly_content)
        monthly_content = common_action.get_text(EmailObjects.Monthly_content[0], EmailObjects.Monthly_content[1])
        self.assertEqual(self.data["MonthlyContent"], monthly_content)
    
    def test_subscribeFlash(self):
        common_action = CommonOperation(self.driver)
        daily_radio = common_action.find_element(EmailObjects.Daily_radio[0], EmailObjects.Daily_radio[1])
        daily_radio.click()
        dailySub_content = common_action.find_element(EmailObjects.DailySub_content[0], EmailObjects.DailySub_content[1])
        time.sleep(1)
        visible_attr = dailySub_content.get_attribute("class")
        self.assertIn("visible", visible_attr)
        time.sleep(3)
        visible_attr_after = dailySub_content.get_attribute("class")
        self.assertNotIn("visible", visible_attr_after)


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testemail("test_subscribeFlash"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)