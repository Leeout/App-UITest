# -*- coding: utf-8 -*-
"""
ios家长端学生登录的用例
"""
import time
from logger import logger
from testIOS.test_data.parents_app.ios_start_page import start_page
from testIOS.test_data.parents_app.ios_login import login
from common.operate_element import operate_element


def __case_collection(driver):
    operate_element(driver, 'ios', **start_page)
    operate_element(driver, 'ios', **login)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    time.sleep(3)
    __case_collection(driver)
    logger.warning('测试结束......')
