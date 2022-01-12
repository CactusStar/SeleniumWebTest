from framework.BasePage import BasePage

class CommonOperation(BasePage):

    def get_exist(self, by, value):
        return self.get_element_exist(by, value)