from framework.BasePage import BasePage

class CommonOperation(BasePage):

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