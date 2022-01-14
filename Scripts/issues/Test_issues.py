import sys
from venv import create
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BaseBrowser import BrowserEngine
from Utilities.Common import CommonOperation
from Utilities.Issues_page import IssuesPage
from Objects.issues_objects import IssuesObjects
from Objects.general_objects import GeneralObjects
import json, time
import unittest
from TestRunner import HTMLTestRunner

class Testissues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_issues_control(self):
        # Navigate to issues page throug general page click Issues items, verify issues page displayed
        issue_page = IssuesPage(self.driver)
        Common = CommonOperation(self.driver)
        Common.click_ele(GeneralObjects.Issues[0], GeneralObjects.Issues[1])
        data = issue_page.load_issues_data()
        self.assertEqual(Common.get_url(), data["pageurl"])
        # Verify the control of the three tabs
        created_exist = Common.get_exist(IssuesObjects.Created[0], IssuesObjects.Created[1])
        self.assertTrue(created_exist)
        created_text = Common.get_text(IssuesObjects.Created[0], IssuesObjects.Created[1])
        self.assertEqual(data["created"], created_text)
        assigned_exist = Common.get_exist(IssuesObjects.Assigned[0], IssuesObjects.Assigned[1])
        self.assertTrue(assigned_exist)
        assigned_text = Common.get_text(IssuesObjects.Assigned[0], IssuesObjects.Assigned[1])
        self.assertEqual(data["assigned"], assigned_text)
        mentioned_exist = Common.get_exist(IssuesObjects.Mentioned[0], IssuesObjects.Mentioned[1])
        self.assertTrue(mentioned_exist)
        mentioned_text = Common.get_text(IssuesObjects.Mentioned[0], IssuesObjects.Mentioned[1])
        self.assertEqual(data["mentioned"], mentioned_text)
        # Verify the Input control
        input_exist = Common.get_exist(IssuesObjects.SearchIssue[0], IssuesObjects.SearchIssue[1])
        self.assertTrue(input_exist)
        # Verify the Open, Closed item
        open_exist = Common.get_exist(IssuesObjects.Open[0], IssuesObjects.Open[1])
        self.assertTrue(open_exist)
        open_text = Common.get_text_inner(IssuesObjects.Open[0], IssuesObjects.Open[1])
        self.assertIn(data["open"], open_text)
        closed_exist = Common.get_exist(IssuesObjects.Closed[0], IssuesObjects.Closed[1])
        self.assertTrue(closed_exist)
        closed_text = Common.get_text_inner(IssuesObjects.Closed[0], IssuesObjects.Closed[1])
        self.assertIn(data["closed"], closed_text)
        # Verify the Visibility, Organization, Sort list
        visibility_exist = Common.get_exist(IssuesObjects.Visibility[0], IssuesObjects.Visibility[1])
        self.assertTrue(visibility_exist)
        vis_text = Common.get_text(IssuesObjects.Visibility[0], IssuesObjects.Visibility[1])
        self.assertEqual(data["Visibility"]["name"], vis_text)
        Common.click_ele(IssuesObjects.Visibility[0], IssuesObjects.Visibility[1])
        vis_header = Common.get_text_inner(IssuesObjects.Visibility_MenuHeader[0], IssuesObjects.Visibility_MenuHeader[1])
        self.assertEqual(data["Visibility"]["header"], vis_header)
        loopcount = len(data["Visibility"]["menulist"])
        for i in range(0, loopcount):
            self.assertEqual(data["Visibility"]["menulist"]["item" + str(i)], Common.find_target_elements(IssuesObjects.Visibility_MenuItems[0], IssuesObjects.Visibility_MenuItems[1])[i].text)
        # Verify the content of the issues

    def test_select_assigned(self):
        issue_page = IssuesPage(self.driver)
        Common = CommonOperation(self.driver)
        Common.click_ele(GeneralObjects.Issues[0], GeneralObjects.Issues[1])
        time.sleep(5)
        Common.click_ele(IssuesObjects.Assigned[0], IssuesObjects.Assigned[1])
        time.sleep(3)
        data = issue_page.load_issues_data()

        self.assertEqual(Common.get_url(), data["assignedurl"])
        # verify the not item match content
        content_text = Common.get_text(IssuesObjects.nomatch_content[0], IssuesObjects.nomatch_content[1])
        self.assertEqual(data["nomatch"], content_text)
        guidance_text = Common.get_text(IssuesObjects.guidance_content[0], IssuesObjects.guidance_content[1])
        self.assertEqual(data["guidance"], guidance_text)

if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testissues("test_select_assigned"))
    # suit.addTest(Testgeneral("test_new_Repositories"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)

