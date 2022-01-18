import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
# from framework.BasePage import BasePage

class NewReopObjects():
    RepoName = ["id", "repository_name"]
    Public_radio = ["id", "repository_visibility_public"]
    Private_radio = ["id", "repository_visibility_private"]
    Add_RM_checkbox = ["id", "repository_auto_init"]
    Add_Ignore_checkbox = ["id", "repository_gitignore_template_toggle"]
    Choose_license_checkbox = ["id", "repository_license_template_toggle"]
    Create_repo_button = ["css", 'button[data-disable-with="Creating repository&hellip;"]']
    ImportRepo_link = ["css", 'a[href="/new/import"]']
    Cancel_button = ["css", 'a[href="/"]']
    Add_RM_Learnmore_link = ["xpath", '//*[@id="new_repository"]/div[4]/div[4]/div[1]/span/a']
    License_hiden_list = ["xpath", '//*[@id="new_repository"]/div[4]/div[4]/div[3]/span[2]']
    