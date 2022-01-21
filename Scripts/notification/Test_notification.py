import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
from Objects.notification_objects import NotificationObjects
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
import time
from framework.BaseBrowser import BrowserEngine

class Testnotification(unittest.TestCase):
    data_path = './Assets/data/notification_data/notification_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_verificationMessage(self):
        common_action = CommonOperation(self.driver)
        common_action.find_element(NotificationObjects.Settings_button[0], NotificationObjects.Settings_button[1]).click()
        time.sleep(3)
        common_action.find_element(NotificationObjects.CreateFilter_button[0], NotificationObjects.CreateFilter_button[1]).click()
        common_action.find_element(NotificationObjects.Create_button[0], NotificationObjects.Create_button[1]).click()
        message = common_action.find_element(NotificationObjects.Create_input[0], NotificationObjects.Create_input[1]).get_attribute("validationMessage")
        self.assertEqual(self.data["validationMessage"], message)
    
    def test_notificationTooltip(self):
        common_action = CommonOperation(self.driver)
        notifcation_button = common_action.find_element(NotificationObjects.Notification_button[0], NotificationObjects.Notification_button[1])
        # message = ActionChains.move_to_element(self.driver, to_element=notifcation_button).getText()
        # message = ActionChains(self.driver).move_to_element(notifcation_button).getText()
        message = notifcation_button.get_attribute("aria-label")
        self.assertEqual(self.data["tooltip"], message)


if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testnotification("test_notificationTooltip"))

    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)