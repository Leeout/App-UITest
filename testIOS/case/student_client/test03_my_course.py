"""
ios学生端 查看学生【我的课程】的用例
"""
import time
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.my_course import my_course


def __case_collection(driver, platform):
    operate_element(driver, platform, **login)
    operate_element(driver, platform, **my_course)


def enter_my_course(driver):
    logger.warning('测试开始......')
    time.sleep(3)
    __case_collection(driver, 'iPad')
    logger.warning('测试结束......')
