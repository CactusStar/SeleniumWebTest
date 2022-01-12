import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from selenium import webdriver
from framework.BasePage import BasePage
import json
import unittest
from Objects.general_objects import GeneralObjects
from Utilities.General_page import GeneralPage
from framework.BasePage import BasePage
from TestRunner import HTMLTestRunner
import time
from framework.BaseBrowser import BrowserEngine

class Testgeneral(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_allExistingControl(self):
        generalpage = GeneralPage(self.driver)
        repositories_exist = generalpage.get_exist(GeneralObjects.Repositories[0], GeneralObjects.Repositories[1])
        explore_repositories_exist = generalpage.get_exist(GeneralObjects.Explore_Repositories[0], GeneralObjects.Explore_Repositories[1])
        self.assertTrue(repositories_exist)
        self.assertTrue(explore_repositories_exist)
        pull_request_exist = generalpage.get_exist(GeneralObjects.Pull_Request[0], GeneralObjects.Pull_Request[1])
        self.assertTrue(pull_request_exist)
        pullrequest_text = generalpage.get_text(GeneralObjects.Pull_Request[0], GeneralObjects.Pull_Request[1])
        self.assertEqual(pullrequest_text, "Pull requests")

    def test_new_Repositories(self):
        """Test new repositories"""
        generalpage = GeneralPage(self.driver)
        newbutton = generalpage.find_target_element(GeneralObjects.NewRepositories[0], GeneralObjects.NewRepositories[1])
        general_data = generalpage.load_general_data()
        newbutton.click()
        # self.UserData_skiplogin(general_data["url_new"])
        text = generalpage.execute_target_script(scripts=general_data["geticonscript"])
        self.assertEqual(text, '"*"')

if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testgeneral("test_allExistingControl"))
    suit.addTest(Testgeneral("test_new_Repositories"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)
    # Testgeneral = Testgeneral()
    # Testgeneral.test_allExistingControl()