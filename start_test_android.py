# -*- coding: utf-8 -*-
"""
运行android测试的入口
"""
import unittest
from config.device.android import device_info
from testAndroid.test_case.parents_app.test1_android_student_login import student_login


class AppTests(unittest.TestCase):
    def setUp(self):
        self.driver = device_info()  # 初始化加载android设备

    def tearDown(self):
        self.driver.quit()  # case执行完退出

    def test_run_case(self):
        student_login(self.driver)  # 学生登录


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AppTests("test_run_case"))
