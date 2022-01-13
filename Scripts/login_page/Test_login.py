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

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def get_login(self):
        with open('./Assets/data/login_data/logininfo.json','r',encoding='utf8') as jdata:
            logindata = json.load(jdata)
            return logindata

    def test_normal_login(self):
        loginpage = LoginPage(self.driver)
        Common = CommonOperation(self.driver)
        logindata = self.get_login()
        username = logindata["username"]
        password = logindata["password"]
        loginpage.type(LoginObjects.Username[0], LoginObjects.Username[1], text=username)
        loginpage.type(LoginObjects.Password[0], LoginObjects.Password[1], text=password)
        Common.click_ele(LoginObjects.Signin[0], LoginObjects.Signin[1])
        current_url = loginpage.get_url()
        self.assertEqual(current_url, "https://github.com/")
    
    def test_invalid_password(self):
        loginpage = LoginPage(self.driver)
        Common = CommonOperation(self.driver)
        logindata = self.get_login()
        username = logindata["username"]
        password = logindata["incorrect_password"]
        loginpage.type(LoginObjects.Username[0], LoginObjects.Username[1], text=username)
        loginpage.type(LoginObjects.Password[0], LoginObjects.Password[1], text=password)
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
