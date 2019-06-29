"""
ios学生端 【公开课】的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from student_client.element.open_class import open_class


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    main_operate(driver, platform, **open_class)


def enter_open_class(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
