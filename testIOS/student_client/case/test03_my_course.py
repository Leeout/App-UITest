"""
ios学生端 【我的课程】的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from testIOS.student_client.element.my_course import my_course


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    main_operate(driver, platform, **my_course)


def enter_my_course(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
