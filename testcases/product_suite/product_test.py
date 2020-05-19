import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.product_action import ProductAction
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class ProductTest(SeleniumBaseCase):
    test_class_data = TestDataUtils('product_suite', 'product_test').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_goto_product']['isnot'], '')
    def test_goto_product(self):
        test_function_data = self.test_class_data['test_goto_product']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        product_action = ProductAction(main_page.driver)
        product_page = product_action.goto_product()
        actual_result = product_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, 'test_goto_product用例不通过')


if __name__ == '__main__':
    unittest.main()
