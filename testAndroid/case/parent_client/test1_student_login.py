"""
android家长端学生登录的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from testAndroid.element.parent_client.login import login


def __case_collection(driver, platform):
    main_operate(driver, platform, **login)


def student_login(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'android')
    logger.warning('测试结束......')
