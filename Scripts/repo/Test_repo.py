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
        common_action.find_element(RepoObjects.ReadMe_button[0], RepoObjects.ReadMe_button[1]).click()
        full_text = common_action.get_text(RepoObjects.Editplace_editbox[0], RepoObjects.Editplace_editbox[1])
        final_text = full_text.split("\n")[1]
        self.assertEqual(self.data["Content"]["item0"], final_text)
        full_text_control = common_action.find_element(RepoObjects.Editplace_editbox[0], RepoObjects.Editplace_editbox[1])
        full_text_control.click()
        # ActionChains(self.driver).send_keys(KEY_ENTER).perform()
        full_text_control.send_keys(Keys.ENTER)
        full_text_control.send_keys("abc")
        lines = common_action.find_elements(RepoObjects.lines_edit[0], RepoObjects.lines_edit[1])
        loopcount = len(self.data["Content"])
        for i in range(0, loopcount):
            self.assertEqual(self.data["Content"]["item"+str(i)], lines[i].text)
    
    def test_navigationHover(self): 
        common_action = CommonOperation(self.driver)
        firstline = common_action.find_element(RepoObjects.firstline_row[0], RepoObjects.firstline_row[1])
        common_action.Hover(firstline)
        haveFocus = firstline.get_attribute("class")
        self.assertIn("navigation-focus", haveFocus)

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Testrepo("test_navigationHover"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)