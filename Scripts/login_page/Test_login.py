import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BaseBrowser import BrowserEngine
from Utilities.Login_page import LoginPage
from Utilities.Common import CommonOperation
from Objects.login_objects import LoginObjects
import json, time
import unittest
from TestRunner import HTMLTestRunner

class TestLoginPage (unittest.TestCase):
    data_path = './Assets/data/login_data/logininfo.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_normal_login(self):
        Common = CommonOperation(self.driver)
        username = self.data["username"]
        password = self.data["password"]
        Common.type_in(LoginObjects.Username[0], LoginObjects.Username[1], text=username)
        Common.type_in(LoginObjects.Password[0], LoginObjects.Password[1], text=password)
        Common.click_ele(LoginObjects.Signin[0], LoginObjects.Signin[1])
        current_url = Common.get_url()
        self.assertEqual(current_url, "https://github.com/")
    
    def test_invalid_password(self):
        Common = CommonOperation(self.driver)
        username = self.data["username"]
        password = self.data["incorrect_password"]
        Common.type_in(LoginObjects.Username[0], LoginObjects.Username[1], text=username)
        Common.type_in(LoginObjects.Password[0], LoginObjects.Password[1], text=password)
        Common.click_ele(LoginObjects.Signin[0], LoginObjects.Signin[1])
        exist = Common.get_exist(LoginObjects.IncorrectInfo[0], LoginObjects.IncorrectInfo[1])
        self.assertTrue(exist)

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestLoginPage("test_invalid_password"))
    # suit.addTest(TestLoginPage("test_normal_login"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)
