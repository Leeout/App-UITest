"""
ios学生端 【口语练习】的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from student_client.element.oral_practice import oral_practice


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    main_operate(driver, platform, **oral_practice)


def enter_oral_practice(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
