"""
ios学生端 【百宝箱】的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.baibao_box import baibao_box


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    operate_element(driver, platform, **baibao_box)


def enter_baibao_box(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'iPad')
    logger.warning('测试结束......')
