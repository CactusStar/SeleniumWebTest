import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
# from framework.BasePage import BasePage

class NotificationObjects():
    Settings_button = ["xpath", '//*[@id="js-repo-pjax-container"]/div/div[2]/nav/div[1]/span[2]/details/summary']
    Filters_dialog = ["css", 'details-dialog[src="/notifications/beta/custom_inboxes_dialog"]']
    CreateFilter_button = ["css", '.js-custom-inbox-create-button']
    Create_button = ["css", ".btn-primary.btn.ml-2"]
    Create_input = ["css", ".form-control.width-full.js-custom-inbox-name-input"]
    Notification_button = ["css", 'a[href="/notifications"]']