"""
ios学生端 学生登录的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login


def __case_collection(driver, platform):
    operate_element(driver, platform, **login)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'iPad')
    logger.warning('测试结束......')
