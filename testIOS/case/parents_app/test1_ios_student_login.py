# -*- coding: utf-8 -*-
"""
ios家长端学生登录的用例
"""
import time
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.parents_app.ios_start_page import start_page
from testIOS.element.parents_app.ios_login import login
from testIOS.element.parents_app.ios_home_page_oral_practice import home_page_oral_practice


def __case_collection(driver):
    operate_element(driver, 'ios', **start_page)
    operate_element(driver, 'ios', **login)
    operate_element(driver, 'ios', **home_page_oral_practice)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    time.sleep(3)
    __case_collection(driver)
    logger.warning('测试结束......')
