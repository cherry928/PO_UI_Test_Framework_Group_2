import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser


class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('main','main_page').get_element_info()
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']
        self.project_menu = elements['project_menu']
        self.product_menu = elements['product_menu']

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def goto_product(self):
        self.click(self.product_menu)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):
        self.click( self.quit_button )

    def goto_project(self): # 进入迭代
        self.click(self.project_menu)

if __name__ == '__main__':
    driver = Browser().get_driver()
    # driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    # main_page = LoginAction(driver).default_login()
    # value = main_page.get_username()
    # print(value)


