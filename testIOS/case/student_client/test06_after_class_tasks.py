"""
ios学生端 【课后任务】的用例
"""
from common.logger import logger
from common.operate_element import operate_element

from testIOS.element.student_client.login import login
from testIOS.element.student_client.after_class_tasks import after_class_tasks


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    operate_element(driver, platform, **after_class_tasks)


def enter_after_class_tasks(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'iPad')
    logger.warning('测试结束......')
