from framework.BasePage import BasePage
import json

class CommonOperation(BasePage):

    def load_data(self, path):
        with open(path,'r',encoding='utf8') as jsondata:
            jsondata = json.load(jsondata)
        return jsondata

    def wait_until(self, seconds):
        self.wait(seconds)

    def get_exist(self, by, value):
        return self.get_element_exist(by, value)
    
    def click_ele(self, by, value):
        self.click(by, value)
    
    def get_url(self):
        return self.get_current_url()
    
    def get_text(self, by, value):
        return self.get_element_text(by, value)
    
    def get_text_inner(self, by, value):
        return self.get_element_text_inner(by, value)
    
    def find_target_elements(self, by, value):
        return self.find_elements(by, value)
    
    def find_target_element(self, by, value):
        return self.find_element(by, value)
    
    def type_in(self, by, value, text):
        self.type(by, value, text)

    def get_driver_handle(self):
        n = self.driver.window_handles
        return n
    
    def switch_windows_handle(self, m):
        n = self.get_driver_handle()
        self.driver.switch_to_window(n[m])
    
    def refresh_current(self):
        self.refresh_page()
    
    def move_mousescroll(self, element): 
        self.move_mousescroll_target(element)
    
    def Hover(self, element):
        self.mouseHover(element)