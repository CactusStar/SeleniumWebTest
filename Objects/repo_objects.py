import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class RepoObjects(BasePage):
    ReadMe_button = ["xpath", '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[4]/a']
    Editplace_editbox = ["id", "code-editor"]
    lines_edit = ["xpath", '//*[@id="code-editor"]/div/pre/span']

