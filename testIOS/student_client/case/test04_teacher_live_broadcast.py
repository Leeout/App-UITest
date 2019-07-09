"""
ios学生端 【外教直播课】的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from testIOS.student_client.element.teacher_live_broadcast import teacher_live_broadcast


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    main_operate(driver, platform, **teacher_live_broadcast)


def enter_teacher_live_broadcast(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
