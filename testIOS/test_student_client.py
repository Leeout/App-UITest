"""
运行iPad测试的入口
"""
import unittest

from common import HTMLTestRunner
from common import output_report
from common.operate_element import failed_retry
from config.connect_ios import setup_ios_device

from testIOS.student_client.case.test01_student_login import setup_page_student_login
from testIOS.student_client.case.test02_student_info import view_student_info
from testIOS.student_client.case.test03_my_course import enter_my_course
from testIOS.student_client.case.test04_teacher_live_broadcast import enter_teacher_live_broadcast
from testIOS.student_client.case.test05_open_class import enter_open_class
from testIOS.student_client.case.test06_after_class_tasks import enter_after_class_tasks
from testIOS.student_client.case.test07_audio_picture_book import enter_audio_picture_book
from testIOS.student_client.case.test08_oral_practice import enter_oral_practice
from testIOS.student_client.case.test09_baibao_box import enter_baibao_box


class AppTests(unittest.TestCase):
    @classmethod  # 通过加装饰器，可让继承unittest.TestCase类的方法只执行一次setUp和tearDown
    def setUpClass(cls):
        cls.driver = setup_ios_device()  # 初始化加载iPad设备

    @classmethod
    def tearDownClass(cls):
        pass  # case执行完不退出设备

    @failed_retry(setUpClass, tearDownClass, 3)
    def test01_student_login(self):
        setup_page_student_login(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test02_student_info(self):
        view_student_info(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test03_enter_my_course(self):
        enter_my_course(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test04_enter_teacher_live_broadcast(self):
        enter_teacher_live_broadcast(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test05_enter_open_class(self):
        enter_open_class(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test06_enter_after_class_tasks(self):
        enter_after_class_tasks(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test07_enter_audio_picture_book(self):
        enter_audio_picture_book(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test08_enter_oral_practice(self):
        enter_oral_practice(self.driver)

    @failed_retry(setUpClass, tearDownClass, 3)
    def test09_enter_baibao_box(self):
        enter_baibao_box(self.driver)


def __add_suite():
    suite = unittest.TestSuite()
    suite.addTest(AppTests("test01_student_login"))
    # suite.addTest(AppTests("test02_student_info"))
    # suite.addTest(AppTests("test03_enter_my_course"))
    # suite.addTest(AppTests("test04_enter_teacher_live_broadcast"))
    # suite.addTest(AppTests("test05_enter_open_class"))
    # suite.addTest(AppTests("test06_enter_after_class_tasks"))
    # suite.addTest(AppTests("test07_enter_audio_picture_book"))
    # suite.addTest(AppTests("test08_enter_oral_practice"))
    # suite.addTest(AppTests("test09_enter_baibao_box"))
    return suite


def run_suite(path):
    """
    :param path: 存放测试报告的路径
    """
    suite = __add_suite()
    file_name = 'student_client_test_report.html'
    # 执行测试
    file = output_report.fileopen(path, file_name)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file,
        title=u'student_client',
        description=u'测试用例执行结果'
    )
    result = runner.run(suite)
    file.close()
    return result
