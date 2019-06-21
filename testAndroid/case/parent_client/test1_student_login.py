"""
android家长端学生登录的用例
"""
import time
from common.logger import logger
from common.operate_element import operate_element

from testAndroid.element.parent_client.login import login


def __case_collection(driver, platform):
    operate_element(driver, platform, **login)


def student_login(driver):
    logger.warning('测试开始......')
    time.sleep(3)
    __case_collection(driver, 'android')
    logger.warning('测试结束......')
