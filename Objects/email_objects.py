import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class EmailObjects(BasePage):
    None_label = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[1]']
    None_radio = ["id", "kind_unsubscribe"]
    None_content = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[1]/p']
    Daily_label = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[2]']
    Daily_radio = ["id", "kind_daily"]
    Daily_content = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[2]/p']
    Weekly_label = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[3]']
    Weekly_radio = ["id", "kind_weekly"]
    Weekly_content = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[3]/p']
    Monthly_label = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[4]']
    Monthly_radio = ["id", "kind_monthly"]
    Monthly_content = ["xpath", '//*[@id="js-pjax-container"]/div[3]/form/div/label[4]/p']
    