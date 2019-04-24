# -*- coding: utf-8 -*-
"""
家长端学生登录的用例
"""
from logger import logger
from login_data import login
from operate_element import operate_element


def student_login(driver):
    logger.warning('测试开始......')
    operate_element(driver, **login)
    logger.warning('测试结束......')
