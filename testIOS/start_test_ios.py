# -*- coding: utf-8 -*-
"""
运行ios测试的入口
"""
import os
import unittest
import HtmlTestRunner
from common.time_base import get_current_time
from config.connect_ios import setup_ios_device

from testIOS.case.parents_app.test1_ios_student_login import setup_page_student_login

get_file = os.path
path = get_file.dirname(get_file.realpath(__file__))
yaml = get_file.join(path, "../report/screenshot/ios")


class AppTests(unittest.TestCase):
    def setUp(self):
        self.driver = setup_ios_device()  # 初始化加载ios设备

    def tearDown(self):
        # self.driver.quit()  # case执行完退出
        pass  # case执行完不退出

    def test_run_case(self):
        setup_page_student_login(self.driver)  # 学生登录


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AppTests("test_run_case"))

    filename = yaml + 'App_UI自动化测试报告' + get_current_time() + '.html'
    file = open(filename, 'wb')
    runner = HtmlTestRunner.HTMLTestRunner(
        output='test_report',
        report_title='App_UI自动化测试报告',
    )
    runner.run(suite)
    file.close()
