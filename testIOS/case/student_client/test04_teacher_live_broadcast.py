"""
ios学生端 【外教直播课】的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.teacher_live_broadcast import teacher_live_broadcast


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    operate_element(driver, platform, **teacher_live_broadcast)


def enter_teacher_live_broadcast(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
