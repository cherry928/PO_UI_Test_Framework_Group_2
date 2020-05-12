#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:create_new_iteration_test.py
# @time:2020/5/12 6:36 下午

import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.create_new_iteration_action import CreateNewIterationAction
from common.config_utils import local_config
from common.test_data_utils import TestDataUtils


class CreateNewIterationTest(unittest.TestCase):

    test_class_data = TestDataUtils('iteration_suite', 'iteration_test').convert_exceldata_to_testdata()
    print(test_class_data)

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    @unittest.skipIf(test_class_data['test_create_new_iteration']['isnot'], '')
    def test_create_new_iteration(self):
        test_function_data = self.test_class_data['test_create_new_iteration']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        print(test_function_data['test_parameter'].get('iteration_name'))
        main_page.goto_project()
        create_new_iteration_action = CreateNewIterationAction(self.base_page.driver)
        create_new_iteration_action.create_new_iterationaction(test_function_data['test_parameter'].get('iteration_name'),
                                                                               test_function_data['test_parameter'].get('iteration_code'),
                                                                               test_function_data['test_parameter'].get('start_date'),
                                                                               test_function_data['test_parameter'].get('close_date'),
                                                                               test_function_data['test_parameter'].get('team_name'),
                                                                               test_function_data['test_parameter'].get('iterative_description')
                                                                               )


if __name__=='__main__':
    unittest.main()
