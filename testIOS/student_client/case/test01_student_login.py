"""
ios学生端 登录的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from student_client.element.login import login


def __case_collection(driver, platform):
    main_operate(driver, platform, **login)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
