import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.product_action import ProductAction, AddProductAction
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class AddProductTest(SeleniumBaseCase):
    test_class_data = TestDataUtils('product_suite', 'product_test').convert_exceldata_to_testdata()

    @unittest.skipIf(test_class_data['test_goto_add_product']['isnot'], '')
    def test_goto_add_product(self):
        test_function_data = self.test_class_data['test_goto_add_product']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),
                                               test_function_data['test_parameter'].get('password'))
        product_action = ProductAction(main_page.driver)
        product_page = product_action.goto_product()
        add_product_action = AddProductAction(product_page.driver)
        add_product_page = add_product_action.goto_add_product()
        actual_result = add_product_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']), True, 'test_goto_add_product用例测试不通过')

    # def test_add_product_name_null(self):
    #     test_function_data = self.test_class_data['test_add_product_name_null']
    #     self.login_action = LoginAction(self.base_page.driver)
    #     main_page = self.login_action.login_success(test_function_data['test_parameter'].get('username'),
    #                                                 test_function_data['test_parameter'].get('password'))
        product_action = main_page.goto_product()
        # product_page = product_action.
        # add_product_action = AddProductAction(product_page.driver)
        # add_product_page = add_product_action.add_product_succeed(test_function_data['test_parameter'].get('product_name'),
        #                                                           test_function_data['test_parameter'].get('product_code'))
        # actual_result = add_product_page.get_product_name_null_text()
        # self.assertEqual(actual_result, test_function_data['excepted_result'], 'test_add_product_name_null用例测试不通过')


if __name__ == '__main__':
    unittest.main()
