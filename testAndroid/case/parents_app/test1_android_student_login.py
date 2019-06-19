# -*- coding: utf-8 -*-
"""
android家长端学生登录的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testAndroid.element.parents_app.android_login import login


def student_login(driver):
    logger.warning('测试开始......')
    operate_element(driver, 'android', **login)
    logger.warning('测试结束......')
