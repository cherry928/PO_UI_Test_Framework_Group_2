from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('login','login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    def input_username(self,username): #方法 == 》控件的操作
        self.input( self.username_inputbox , username )

    def input_password(self,password):
        self.input( self.password_inputbox , password )

    def click_login(self):
        self.click( self.login_button )

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()

if __name__=="__main__":
    driver = Browser().get_driver()
    login_page =  LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.screenshot_as_file()


