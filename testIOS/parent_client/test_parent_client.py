"""
运行ios测试的入口
"""
import unittest

from config.connect_ios import setup_ios_device

from testIOS.parent_client.case.test01_student_login import setup_page_student_login


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
