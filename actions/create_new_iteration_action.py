#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:create_new_iteration_action.py
# @time:2020/5/12 1:00 下午

from element_infos.iteration.create_new_iteration_page import CreateNewIterationPage
from element_infos.iteration.iteration_team_management_page import IterationTeamManagement

class CreateNewIterationAction:

    def __init__(self, driver):
        self.create_new_iteration_action = CreateNewIterationPage(driver)

    def create_new_iterationaction(self, iteration_name, iteration_code, start_date, close_date, team_name, iterative_description):
        self.create_new_iteration_action.click_create_iteration()
        self.create_new_iteration_action.input_iteration_name(iteration_name)
        self.create_new_iteration_action.input_iteration_code(iteration_code)
        self.create_new_iteration_action.clear_data_content()
        self.create_new_iteration_action.input_start_date(start_date)
        self.create_new_iteration_action.click_start_date()
        self.create_new_iteration_action.input_close_date(close_date)
        self.create_new_iteration_action.click_close_date()
        self.create_new_iteration_action.input_team_name(team_name)
        self.create_new_iteration_action.click_iteration_type()
        self.create_new_iteration_action.click_chose_iteration_type()
        self.create_new_iteration_action.click_related_items()
        self.create_new_iteration_action.click_chose_related_items()
        self.create_new_iteration_action.switchto_frame()
        self.create_new_iteration_action.input_iterative_description(iterative_description)
        self.create_new_iteration_action.switchto_default_content()
        self.create_new_iteration_action.slide_element()
        self.create_new_iteration_action.click_preservation()
        self.create_new_iteration_action.click_close_button()
        # return IterationTeamManagement(self.create_new_iteration_action.driver)


