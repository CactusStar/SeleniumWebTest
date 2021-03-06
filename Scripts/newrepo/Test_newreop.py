import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
from Objects.NewRepo_objects import NewReopObjects
from Utilities.NewRepo_page import NewRepoPage
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
import time
from framework.BaseBrowser import BrowserEngine

class Testnewrepo(unittest.TestCase):
    data_path = './Assets/data/newrepo_data/newrepo_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_controlstatus(self):
        common_action = CommonOperation(self.driver)
        public_radio = common_action.find_target_element(NewReopObjects.Public_radio[0], NewReopObjects.Public_radio[1])
        private_radio = common_action.find_target_element(NewReopObjects.Private_radio[0], NewReopObjects.Private_radio[1])
        addreadme_checkbox = common_action.find_target_element(NewReopObjects.Add_RM_checkbox[0], NewReopObjects.Add_RM_checkbox[1])
        addignore_checkbox = common_action.find_target_element(NewReopObjects.Add_Ignore_checkbox[0], NewReopObjects.Add_Ignore_checkbox[1])
        chooselicen_checkbox = common_action.find_target_element(NewReopObjects.Choose_license_checkbox[0], NewReopObjects.Choose_license_checkbox[1])
        create_button = common_action.find_target_element(NewReopObjects.Create_repo_button[0], NewReopObjects.Create_repo_button[1])
        self.assertTrue(public_radio.is_selected())
        private_radio.click()
        self.assertFalse(public_radio.is_selected())
        self.assertTrue(private_radio.is_selected())
        self.assertFalse(addreadme_checkbox.is_selected())
        self.assertFalse(addignore_checkbox.is_selected())
        self.assertFalse(chooselicen_checkbox.is_selected())
        addignore_checkbox.click()
        self.assertTrue(addignore_checkbox.is_selected())
        addignore_checkbox.click()
        self.assertFalse(create_button.is_enabled())
        common_action.type_in(NewReopObjects.RepoName[0], NewReopObjects.RepoName[1], self.data["RepoName"])
        time.sleep(3)
        self.assertTrue(create_button.is_enabled())
    
    def test_import_cancel(self):
        common_action = CommonOperation(self.driver)
        import_link = common_action.find_target_elements(NewReopObjects.ImportRepo_link[0], NewReopObjects.ImportRepo_link[1])
        import_link[1].click()
        self.assertEqual(common_action.get_current_url(), self.data["importlink"])
        cancel_button = common_action.find_target_element(NewReopObjects.Cancel_button[0], NewReopObjects.Cancel_button[1])
        cancel_button.click()
        self.assertEqual(common_action.get_current_url(), self.data["cancellink"])

    def test_learnmore(self):
        common_action = CommonOperation(self.driver)
        common_action.find_target_element(NewReopObjects.Add_RM_Learnmore_link[0], NewReopObjects.Add_RM_Learnmore_link[1]).click()
        common_action.switch_windows_handle(-1)
        jump_url = common_action.get_current_url()
        self.assertEqual(self.data["addreadmelearnmore"], jump_url)
    
    def test_hidencontent(self):
        common_action = CommonOperation(self.driver)
        hiden_list = common_action.find_target_element(NewReopObjects.License_hiden_list[0], NewReopObjects.License_hiden_list[1])
        # display_attribute = hiden_list.value_of_css_property("display")
        display_attribute = hiden_list.is_displayed()
        self.assertFalse(display_attribute)
        # self.assertEqual(display_attribute, "none")
        chooselicen_checkbox = common_action.find_target_element(NewReopObjects.Choose_license_checkbox[0], NewReopObjects.Choose_license_checkbox[1])
        chooselicen_checkbox.click()
        # display_attribute = hiden_list.value_of_css_property("display")
        # self.assertEqual(display_attribute, "block")
        display_attribute = hiden_list.is_displayed()
        self.assertTrue(display_attribute)


if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testnewrepo("test_hidencontent"))
    # suit.addTest(Testnewrepo("test_import_cancel"))
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