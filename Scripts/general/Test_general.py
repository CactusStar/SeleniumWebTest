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
        data = generalpage.load_general_data()
        # verify Repositories and Explore repositories exist
        repositories_exist = generalpage.get_exist(GeneralObjects.Repositories[0], GeneralObjects.Repositories[1])
        explore_repositories_exist = generalpage.get_exist(GeneralObjects.Explore_Repositories[0], GeneralObjects.Explore_Repositories[1])
        self.assertTrue(repositories_exist)
        self.assertTrue(explore_repositories_exist)
        #verify the menubar exist and the text is correct
        pull_request_exist = generalpage.get_exist(GeneralObjects.Pull_Request[0], GeneralObjects.Pull_Request[1])
        self.assertTrue(pull_request_exist)
        pullrequest_text = generalpage.get_text(GeneralObjects.Pull_Request[0], GeneralObjects.Pull_Request[1])
        self.assertEqual(pullrequest_text, data["MenuBar1"])
        issues_exist = generalpage.get_exist(GeneralObjects.Issues[0], GeneralObjects.Issues[1])
        self.assertTrue(issues_exist)
        issues_text = generalpage.get_text(GeneralObjects.Issues[0], GeneralObjects.Issues[1])
        self.assertEqual(issues_text, data["MenuBar2"])
        marketplace_exist = generalpage.get_exist(GeneralObjects.Marketplace[0], GeneralObjects.Marketplace[1])
        self.assertTrue(marketplace_exist)
        marketplace_text = generalpage.get_text(GeneralObjects.Marketplace[0], GeneralObjects.Marketplace[1])
        self.assertEqual(marketplace_text, data["MenuBar3"])
        explore_exist = generalpage.get_exist(GeneralObjects.Explore[0], GeneralObjects.Explore[1])
        self.assertTrue(explore_exist)
        explore_text = generalpage.get_text(GeneralObjects.Explore[0], GeneralObjects.Explore[1])
        self.assertEqual(explore_text, data["MenuBar4"])


    def test_new_Repositories(self):
        """Test new repositories"""
        generalpage = GeneralPage(self.driver)
        newbutton = generalpage.find_target_element(GeneralObjects.NewRepositories[0], GeneralObjects.NewRepositories[1])
        general_data = generalpage.load_general_data()
        newbutton.click()
        # self.UserData_skiplogin(general_data["url_new"])
        text = generalpage.execute_target_script(scripts=general_data["geticonscript"])
        self.assertEqual(text, '"*"')

    def test_new_component(self): 
        generalpage = GeneralPage(self.driver)
        
if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testgeneral("test_allExistingControl"))
    # suit.addTest(Testgeneral("test_new_Repositories"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)
    # Testgeneral = Testgeneral()
    # Testgeneral.test_allExistingControl()