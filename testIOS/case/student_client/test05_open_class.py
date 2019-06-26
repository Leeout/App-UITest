"""
ios学生端 【公开课】的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.open_class import open_class


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    operate_element(driver, platform, **open_class)


def enter_open_class(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
