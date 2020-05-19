#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/5/11 20:51
from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config
from actions.login_action import LoginAction
from element_infos.main.main_page import MainPage
from element_infos.product.product_page import ProductPage
from element_infos.product.add_product_page import AddProductPage


class ProductAction:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.product_page = ProductPage(driver)
        self.add_product_page = AddProductPage(driver)
        self.add_product_action = AddProductAction(driver)

    def goto_product(self):
        self.main_page.goto_product()
        return ProductPage(self.product_page.driver)


class AddProductAction(ProductAction):
    def goto_add_product(self):
        self.add_product_page.click_add_product_button()
        return AddProductPage(self.product_page.driver)

    def add_product_succeed(self, product_name, product_code):
        add_product_page = self.add_product_action.goto_add_product()
        add_product_page.sendkeys_product_name_input(product_name)
        add_product_page.sendkeys_product_code_input(product_code)
        add_product_page.target_locator()
        add_product_page.click_save_button()


if __name__ == '__main__':
    driver = Browser().get_driver()
    login = LoginAction(driver)
    bp = BasePage(driver)
    bp.set_browser_max()
    bp.open_url(local_config.url)
    login.login_success('chenjianglin', '1q2w3e4r,')
    # pna = ProductAction(driver)
    # pna.goto_product()
    ad = AddProductAction(driver)
    # ad.goto_add_product()
    ad.add_product_succeed( '', '1q2w3e4r,')




