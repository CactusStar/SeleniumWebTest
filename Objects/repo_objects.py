import sys
from typing import Any
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
    GotoFile_button = ['css', 'a[data-ga-click="Repository, find file, location:repo overview"]']
    Search_input = ['id', 'tree-finder-field']
    ProjectTree_tree = ['id', 'tree-browser']
    Issue_tab = ['id', 'issues-tab']
    NewIssue_button = ['xpath', '//*[@id="repo-content-pjax-container"]/div/div[2]/div[2]']
    Issuetitle_input = ['id', 'issue_title']
    SubmitIssue_button = ['xpath', '//*[@id="new_issue"]/div/div/div[1]/div/div[1]/div/div[2]/button']
    Issuecount_number = ['id', 'issues-repo-tab-count']
    Issueheadline_text = ['xpath', '//*[@id="partial-discussion-header"]/div[1]/div/h1']
    Issue4_link = ['id', 'issue_4_link']
    Comments_textarea = ['id', 'new_comment_field']
    Issue6_link = ['id', 'issue_10_link']
    CloseIssue_button = ['name', 'comment_and_close']
    CloseTime_text = ['xpath', '//*[@id="event-6079327448"]/div[2]/a[3]/relative-time']
    Settings_button = ['xpath', '//*[@id="repo-content-pjax-container"]/div/div[3]/div[2]/div/div[1]/div/details/summary']
