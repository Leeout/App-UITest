# -*- coding: utf-8 -*-
"""
运行测试的入口
"""
import unittest
from android_device import device_info
from test01_student_login import student_login


class AppTests(unittest.TestCase):
    def setUp(self):
        self.driver = device_info()  # 初始化加载安卓设备

    def tearDown(self):
        self.driver.quit()  # case执行完退出

    def test_run_case(self):
        student_login(self.driver)  # 学生登录


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
