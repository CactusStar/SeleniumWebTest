import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
import time
from Objects.repo_objects import RepoObjects
from Utilities.Common import CommonOperation
from TestRunner import HTMLTestRunner
from framework.BaseBrowser import BrowserEngine
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Testrepo(unittest.TestCase):
    data_path = './Assets/data/repo_data/repo_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_fulltext(self):
        common_action = CommonOperation(self.driver)
        common_action.find_target_element(RepoObjects.ReadMe_button[0], RepoObjects.ReadMe_button[1]).click()
        full_text = common_action.get_text(RepoObjects.Editplace_editbox[0], RepoObjects.Editplace_editbox[1])
        final_text = full_text.split("\n")[1]
        self.assertEqual(self.data["Content"]["item0"], final_text)
        full_text_control = common_action.find_target_element(RepoObjects.Editplace_editbox[0], RepoObjects.Editplace_editbox[1])
        full_text_control.click()
        # ActionChains(self.driver).send_keys(KEY_ENTER).perform()
        full_text_control.send_keys(Keys.ENTER)
        full_text_control.send_keys("abc")
        lines = common_action.find_target_elements(RepoObjects.lines_edit[0], RepoObjects.lines_edit[1])
        loopcount = len(self.data["Content"])
        for i in range(0, loopcount):
            self.assertEqual(self.data["Content"]["item"+str(i)], lines[i].text)
    
    def test_navigationHover(self): 
        common_action = CommonOperation(self.driver)
        firstline = common_action.find_target_element(RepoObjects.firstline_row[0], RepoObjects.firstline_row[1])
        common_action.Hover(firstline)
        haveFocus = firstline.get_attribute("class")
        self.assertIn("navigation-focus", haveFocus)

    def test_thirdpartyExtension(self):
        common_action = CommonOperation(self.driver)
        common_action.find_target_element(RepoObjects.sourcegraph_button[0], RepoObjects.sourcegraph_button[1]).click()
        # time.sleep(3)
        common_action.switch_windows_handle(-1)
        common_action.waitload(20)
        jump_url = common_action.get_current_url()
        self.assertEqual(jump_url, self.data["jumpURL"])

        common_action.find_target_element(RepoObjects.DailyTask_treeitem[0], RepoObjects.DailyTask_treeitem[1]).click()
        time.sleep(3)
        dailytask_edit = common_action.find_target_elements(RepoObjects.DailyTask_edit[0], RepoObjects.DailyTask_edit[1])
        expected_text = dailytask_edit[1].text
        self.assertEqual(expected_text, self.data["Head"])

        common_action.switch_windows_handle(0)
        # branch_menu = common_action.find_target_element(RepoObjects.Branch_menu[0], RepoObjects.Branch_menu[1])
        exist = common_action.get_element_text(RepoObjects.Branch_menu[0], RepoObjects.Branch_menu[1])
        self.assertTrue(exist)
    
    def test_gotofileSearch(self): 
        common_action = CommonOperation(self.driver)
        common_action.find_target_element(RepoObjects.GotoFile_button[0], RepoObjects.GotoFile_button[1]).click()
        ul = common_action.find_target_element(RepoObjects.ProjectTree_tree[0], RepoObjects.ProjectTree_tree[1])
        lis_before = ul.find_elements_by_xpath('li')
        count_before = len(lis_before)
        self.assertEqual(count_before, 3)
        common_action.find_target_element(RepoObjects.Search_input[0], RepoObjects.Search_input[1]).click()
        common_action.type_in(RepoObjects.Search_input[0], RepoObjects.Search_input[1], "Auto")
        time.sleep(3)
        # ul = common_action.find_target_element(RepoObjects.ProjectTree_tree[0], RepoObjects.ProjectTree_tree[1])
        lis_after = ul.find_elements_by_xpath('li')
        count_after = len(lis_after)
        self.assertEqual(count_after, 1)

    def test_ButtonExist(self):
        common_action = CommonOperation(self.driver)
        common_action.waitTillObjectExist(RepoObjects.sourcegraph_button[0], RepoObjects.sourcegraph_button[1])
    
    def test_newIssue(self):
        common_action = CommonOperation(self.driver)
        beforecount = common_action.find_target_element(RepoObjects.Issuecount_number[0], RepoObjects.Issuecount_number[1]).text
        common_action.find_target_element(RepoObjects.Issue_tab[0], RepoObjects.Issue_tab[1]).click()
        common_action.waitTillObjectExist(RepoObjects.NewIssue_button[0], RepoObjects.NewIssue_button[1])
        common_action.find_target_element(RepoObjects.NewIssue_button[0], RepoObjects.NewIssue_button[1]).click()
        common_action.type_in(RepoObjects.Issuetitle_input[0], RepoObjects.Issuetitle_input[1], "thisisTest1")
        common_action.waitTillObjectEnabled(RepoObjects.SubmitIssue_button[0], RepoObjects.SubmitIssue_button[1])
        common_action.find_target_element(RepoObjects.SubmitIssue_button[0], RepoObjects.SubmitIssue_button[1]).click()
        common_action.waitTillObjectExist(RepoObjects.Issueheadline_text[0], RepoObjects.Issueheadline_text[1])
        aftercount = common_action.find_target_element(RepoObjects.Issuecount_number[0], RepoObjects.Issuecount_number[1]).text
        self.assertEqual(int(beforecount)+1, int(aftercount))
    
    def test_enterComments(self):
        common_action = CommonOperation(self.driver)
        common_action.find_target_element(RepoObjects.Issue_tab[0], RepoObjects.Issue_tab[1]).click()
        common_action.waitTillObjectExist(RepoObjects.Issue4_link[0], RepoObjects.Issue4_link[1])
        common_action.find_target_element(RepoObjects.Issue4_link[0], RepoObjects.Issue4_link[1]).click()
        common_action.waitTillObjectExist(RepoObjects.Comments_textarea[0], RepoObjects.Comments_textarea[1])
        common_action.find_target_element(RepoObjects.Comments_textarea[0], RepoObjects.Comments_textarea[1]).click()
        common_action.find_target_element(RepoObjects.Comments_textarea[0], RepoObjects.Comments_textarea[1]).send_keys("this is text")
        time.sleep(5)
        value = common_action.find_target_element(RepoObjects.Comments_textarea[0], RepoObjects.Comments_textarea[1]).get_attribute("value")
        self.assertEqual(value, "this is text")

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testrepo("test_enterComments"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)