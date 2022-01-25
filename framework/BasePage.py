from selenium import webdriver
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os,platform, time
import json
import sys
import re
import requests

sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')

logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/SeleniumWebTest/Assets/webdriver/chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def get_token(self):
        
        login_url = "https://github.com/login"
        r = requests.session().get(login_url, headers = self.headers)
        authenticity_token = re.findall('<input type="hidden" name="authenticity_token" value="(.*?)" />', r.text)
        print("authenticity_token：{}".format(authenticity_token))
        return authenticity_token[1]

    def github_login(self, authenticity_token, username, password):
        session_url = "https://github.com/session"
        body = {
            "authenticity_token":authenticity_token,
            "commit":"Sign in",
            "login":username,
            "password":password,
            "utf8":"✓",
            "webauthn-support":"unknown"
        }
        r = self.s.post(session_url, headers = self.headers, data = body)
        title = re.findall('<title>(.+?)</title>',r.text)
        print("title：%s" %title[0])
        return title[0]

    # 通过 title 判断是否登录成功
    def is_login_success(self, title):
        if "GitHub" == title:
            return True
        else:
            return False

    def open_Browser(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    
    # quit browser
    def quitBrowser(self):
        self.driver.quit()
    
    def save_cookies(self):
        project_path = os.path.dirname(os.getcwd())
        file_path = project_path + '/cookies/'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        cookies = self.driver.get_cookies()

        with open(file_path + "yd.cookies", "w") as c:
            json.dump(cookies, c)
        print(cookies)
    
    # go forward
    def forward(self): 
        self.driver.forward()
    # go back
    def back(self):
        self.driver.back()
    # type
    def type(self, by, value, text):
        el = self.find_element(by, value)
        el.clear()
        try:
            el.send_keys(text)
        except NameError as e:
            logger.error("Failed to send key %s" % e)
    # clear
    def clear(self, by, value):
        el = self.find_element(by, value)
        try:
            el.clear()
        except NameError as e:
            logger.error("Failed to clear input box %s" % e)
    # find element
    def find_element(self, by=By.ID, value=None):
        try:
            if by == "id":
                element = self.driver.find_element_by_id(value)
            elif by == "name":
                element = self.driver.find_element_by_name(value)
            elif by == "class":
                element = self.driver.find_element_by_class_name(value)
            elif by == "link_text":
                element = self.driver.find_element_by_link_text(value)
            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value)
            elif by == "tag":
                element = self.driver.find_element_by_tag_name(value)
            elif by == "css":
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
        return element

    def find_elements(self, by=By.ID, value=None):
        try:
            if by == "id":
                elements = self.driver.find_elements_by_id(value)
            elif by == "name":
                elements = self.driver.find_elements_by_name(value)
            elif by == "class":
                elements = self.driver.find_elements_by_class_name(value)
            elif by == "link_text":
                elements = self.driver.find_elements_by_link_text(value)
            elif by == "xpath":
                elements = self.driver.find_elements_by_xpath(value)
            elif by == "tag":
                elements = self.driver.find_elements_by_tag_name(value)
            elif by == "css":
                elements = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
        return elements

    def UserData_skiplogin(self, url):
        if platform.system() =="Windows":
            os.system("taskkill -im chrome* -f")
        else:
            os.system("killall -9 chrome*")

        my_dir = os.path.expanduser("~")

        profile_directory = r'--user-data-dir={}\\AppData\\Local\\Google\\Chrome\\User Data'.format(my_dir)
        print(profile_directory)
        option = webdriver.ChromeOptions()
        option.add_argument(profile_directory)

        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    # click
    def click(self, by, value):
        el = self.find_element(by, value)
        try:
            el.click()
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
    
    def get_element_exist(self, by, value):
        flag = True
        try:
            self.find_element(by, value)
            
        except:
            flag = False
        print(flag)
        return flag 

    def get_element_text(self, by, value):
        return self.find_element(by, value).text

    def get_element_text_inner(self, by, value):
        return self.find_element(by, value).get_attribute("innerText")

    def execute_script(self, script):
        return self.driver.execute_script(script)
    
    def get_token(self):
        token = self.driver.execute_script('window.sessionStorage.getItem("token")')
        return token
    # wait
    def wait(self, seconds):
        self.driver.implicit_wait(seconds)

    # close current window
    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)
    
    def quit_browser(self):
        self.driver.quit()

    def get_current_url(self):
        return self.driver.current_url

    def report_name(self):
        current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return current_time

    def refresh_page(self):
        self.driver.refresh()