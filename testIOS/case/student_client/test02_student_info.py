"""
ios学生端 首页左上角【学生个人信息】的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.my_info import my_info


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    operate_element(driver, platform, **my_info)


def view_student_info(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
