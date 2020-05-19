import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser


class ProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements = ElementdataUtils('product','product_page').get_element_info()
        self.story_page = elements['story_page']
        self.plan_page = elements['plan_page']

    def goto_story_page(self):
        self.click(self.story_page)

    def goto_plan_page(self):
        value = self.get_text(self.plan_page)


if __name__ == '__main__':
    driver = Browser().get_driver()
    # driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    # main_page = LoginAction(driver).default_login()
    # value = main_page.get_username()
    # print(value)


