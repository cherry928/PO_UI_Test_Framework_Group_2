#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/5/16 16:29

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser


class AddProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementdataUtils('product', 'product_page').get_element_info()
        self.add_product_button = elements['add_product_button']
        self.add_product_assert = elements['add_product_assert']
        self.product_name_input = elements['product_name_input']
        self.product_name_null_assert = elements['product_name_null_assert']
        self.product_code_input = elements['product_code_input']
        self.product_line_button = elements['product_line_button']
        self.product_line_name_input = elements['product_line_name_input']
        self.product_line_abbreviation_input = elements['product_line_abbreviation_input']
        self.product_line_add_button = elements['product_line_add_button']
        self.product_line_del_button = elements['product_line_del_button']
        self.product_line_save_button = elements['product_line_save_button']
        self.product_line_back_button = elements['product_line_back_button']
        self.product_line_close_button = elements['product_line_close_button']
        self.product_principal_button = elements['product_principal_button']
        self.product_principal_choice = elements['product_principal_choice']
        self.test_principal_button = elements['test_principal_button']
        self.test_principal_choice = elements['test_principal_choice']
        self.issue_principal_button = elements['issue_principal_button']
        self.issue_principal_choice = elements['issue_principal_choice']
        self.product_describe_input = elements['product_describe_input']
        self.default_choice_visit = elements['default_choice_visit']
        self.private_choice_visit = elements['private_choice_visit']
        self.custom_choice_visit = elements['custom_choice_visit']
        self.save_button = elements['save_button']
        self.back_button = elements['back_button']

    def click_add_product_button(self):
        self.click(self.add_product_button)

    def sendkeys_product_name_input(self, content):
        self.input(self.product_name_input, content)

    def sendkeys_product_code_input(self, content):
        self.input(self.product_code_input, content)

    def click_product_line_button(self):
        self.click(self.product_line_button)

    def sendkeys_product_line_name_input(self, content):
        self.input(self.product_line_name_input, content)

    def click_save_button(self):
        self.click(self.save_button)

    # ---断言
    def get_add_product_text(self):
        self.get_text(self.add_product_assert)

    def get_product_name_null_text(self):
        value = self.get_text(self.product_name_null_assert)
        return value


if __name__ == '__main__':
    driver = Browser().get_driver()
    # driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    # main_page = LoginAction(driver).default_login()
    # value = main_page.get_username()
    # print(value)
