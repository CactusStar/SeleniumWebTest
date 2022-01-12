# -*- coding:utf-8 -*-
import sys
sys.path.append('C://Users//XHe1//Desktop//MyProject//SeleniumWebTest')
import os.path
import platform
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/SeleniumWebTest/Assets/webdriver/chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config.ini file, return the driver

    def open_browser(self, driver):
        # 读取配置配件
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/SeleniumWebTest/Assets/config/config.ini'
        config.read(file_path)

        # 获取配置文件属性
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)
        login = config.get("loginNeed", "value")

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            if login == "False":
                if platform.system() =="Windows":
                    os.system("taskkill -im chrome* -f")
                else:
                    os.system("killall -9 chrome*")

                my_dir = os.path.expanduser("~")

                profile_directory = r'--user-data-dir={}\\AppData\\Local\\Google\\Chrome\\User Data'.format(my_dir)
                print(profile_directory)
                option = webdriver.ChromeOptions()
                option.add_argument(profile_directory)

                driver = webdriver.Chrome(chrome_options=option)
            else:
                driver = webdriver.Chrome(self.chrome_driver_path)
                logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

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

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()