import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class RepoObjects(BasePage):
    ReadMe_button = ["xpath", '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[4]/a']
    Editplace_editbox = ["id", "code-editor"]
    lines_edit = ["xpath", '//*[@id="code-editor"]/div/pre/span']
    firstline_row = ['xpath', '//*[@id="repo-content-pjax-container"]/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]']
    sourcegraph_button = ["id", "open-on-sourcegraph"]
    DailyTask_treeitem = ['css', 'a[title="DailyTask.md"]']
    DailyTask_edit = ['tag', 'h1']
    Branch_menu = ["id", "branch-select-menu"]

