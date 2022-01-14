import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class IssuesObjects(BasePage):
    Created= ["css", 'a[aria-label="Issues created by you"]']
    Assigned = ["css", 'a[aria-label="Issues assigned to you"]']
    Mentioned = ["css", 'a[title="Issues mentioning you"]']
    SearchIssue = ["id", "js-issues-search"]
    Open = ["xpath", '//*[@id="js-pjax-container"]/div/div[2]/div/a[1]']
    Closed = ["css", 'a[data-ga-click="Issues, Table state, Closed"]']
    Visibility = ["id", "visiblity-select-menu"]
    Organization = ["id", "orgs-select-menu"]
    Sort = ["id", "sort-select-menu"]
    Visibility_MenuHeader = ["xpath", '//*[@id="visiblity-select-menu"]/details-menu/div/div[1]/span']
    Visibility_MenuItems = ["xpath", '//*[@id="visiblity-select-menu"]/details-menu/div/div[2]/a/span']
    Organization_MenuHeader = ["xpath", '//*[@id="orgs-select-menu"]/details-menu/div/div[1]/span']
    Organization_input = ["id", "orgs-filter-field"]
    Sort_MenuHeader = ["xpath", '//*[@id="sort-select-menu"]/details-menu/div/header/span']
    Sort_MenuItems = ["xpath", '//*[@id="sort-select-menu"]/details-menu/div/div/a[1]/span']
    Content_project_title = ["xpath", '//*[@id="issue_34_dreambo8563_vue-particle-effect-buttons"]/div/div[2]/a']
    Content_date = ["xpath", '//*[@id="issue_34_dreambo8563_vue-particle-effect-buttons"]/div/div[2]/div/span[1]']

    nomatch_content = ["xpath", '//*[@id="js-issues-toolbar"]/div[2]/div/h3']
    guidance_content = ["xpath", '//*[@id="js-issues-toolbar"]/div[2]/div/p']