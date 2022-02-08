import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
from framework.BasePage import BasePage

class PortalObjects(BasePage):
    Firstline_input = ["xpath", '//*[@id="home-code"]/div/div/div[4]/ul/li[3]/div/div[2]/div/div/div/div[1]/span']
    Otherlines_input = ['xpath', '//*[@id="home-code"]/div/div/div[4]/ul/li[3]/div/div[2]/div/div/div/div']