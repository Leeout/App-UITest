# -*- coding: utf-8 -*-
"""
ios学生端 学生登录的用例
"""
import time
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login


def __case_collection(driver):
    operate_element(driver, 'ios', **login)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    time.sleep(3)
    __case_collection(driver)
    logger.warning('测试结束......')
