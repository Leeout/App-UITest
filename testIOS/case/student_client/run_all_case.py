"""
ios学生端 所有的用例
"""
from common.logger import logger
from testIOS.case.student_client.test01_student_login import setup_page_student_login
from testIOS.case.student_client.test02_student_info import view_student_info
from testIOS.case.student_client.test03_my_course import enter_my_course


def run_all_case(driver):
    logger.warning('执行所有测试用例开始......')
    setup_page_student_login(driver)
    view_student_info(driver)
    enter_my_course(driver)
    logger.warning('执行所有测试用例结束......')
