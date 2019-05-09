# -*- coding: utf-8 -*-
"""
ios家长端学生登录的用例
"""
import time
from logger import logger
from ios_start_page import start_page
from ios_home_page import home_page
from ios_login import login
from operate_element import scroll_screen, operate_element


def __case_collection(driver):
    # scroll_screen(driver)
    # operate_element(driver, 'ios', **start_page)
    # operate_element(driver, 'ios', **home_page)
    operate_element(driver, 'ios', **login)


def student_login(driver):
    logger.warning('测试开始......')
    time.sleep(6)
    __case_collection(driver)
    logger.warning('测试结束......')
