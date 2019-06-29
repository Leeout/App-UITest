"""
ios家长端 学生登录的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from parent_client.element.login import login


def __case_collection(driver, platform):
    main_operate(driver, platform, **login)


def setup_page_student_login(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ios')
    logger.warning('测试结束......')
