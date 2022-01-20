import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import unittest
import time
from Objects.popup_objects import PopupObjects
from Utilities.Common import CommonOperation
from Utilities.popup_page import PopupPage
from TestRunner import HTMLTestRunner
from framework.BaseBrowser import BrowserEngine

class Testpopup(unittest.TestCase):
    data_path = './Assets/data/general_data/general_data.json'
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.data = browse.load_data(cls.data_path)
        cls.driver = browse.open_browser(cls, cls.data_path)

    def test_Edit_dialog(self):
        common_action = CommonOperation(self.driver)
        common_action.click_ele(PopupObjects.User_Dropdown[0], PopupObjects.User_Dropdown[1])
        time.sleep(3)
        common_action.click_ele(PopupObjects.Profile_status[0], PopupObjects.Profile_status[1])
        # verify dialog pops up
        dialog_exist = common_action.get_exist(PopupObjects.Edit_Dialog[0], PopupObjects.Edit_Dialog[1])
        self.assertTrue(dialog_exist)

        

if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testpopup("test_Edit_dialog"))
    # suit.addTest(Testgeneral("test_new_Repositories"))
    with(open('TestReport/' + time.strftime('%Y%m%d%H%M',time.localtime(time.time())) + '.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='<Test Github>Test Report',
            description='Description: This is for github general page test'
        )
        runner.run(suit)