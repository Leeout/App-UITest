"""
运行iPad测试的入口
"""
import sys
import unittest

from common import output_report
from common import HTMLTestRunner_cn
from common.ding_push import ding_message_push
from common.get_test_result import get_report_data
from config.api.dingding_api import API
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
    @classmethod  # 加装饰器，可让继承unittest.TestCase类的方法只执行一次setUp和tearDown
    def setUpClass(cls):
        cls.driver = setup_ios_device()  # 初始化加载iPad设备

    @classmethod
    def tearDownClass(cls):
        pass  # case执行完不退出设备

    @unittest.skip("学生登录")
    def test01_student_login(self):
        setup_page_student_login(self.driver)

    def test02_student_info(self):
        view_student_info(self.driver)

    def test03_enter_my_course(self):
        enter_my_course(self.driver)

    def test04_enter_teacher_live_broadcast(self):
        enter_teacher_live_broadcast(self.driver)

    def test05_enter_open_class(self):
        enter_open_class(self.driver)

    @unittest.skip("课后作业")
    def test06_enter_after_class_tasks(self):
        enter_after_class_tasks(self.driver)

    def test07_enter_audio_picture_book(self):
        enter_audio_picture_book(self.driver)

    def test08_enter_oral_practice(self):
        enter_oral_practice(self.driver)

    def test09_enter_baibao_box(self):
        enter_baibao_box(self.driver)


def __add_suite():
    suite = unittest.TestSuite()
    suite.addTest(AppTests("test01_student_login"))
    suite.addTest(AppTests("test02_student_info"))
    suite.addTest(AppTests("test03_enter_my_course"))
    suite.addTest(AppTests("test04_enter_teacher_live_broadcast"))
    suite.addTest(AppTests("test05_enter_open_class"))
    suite.addTest(AppTests("test06_enter_after_class_tasks"))
    suite.addTest(AppTests("test07_enter_audio_picture_book"))
    suite.addTest(AppTests("test08_enter_oral_practice"))
    suite.addTest(AppTests("test09_enter_baibao_box"))
    return suite


def run_suite(path):
    """
    :param path: 存放测试报告的路径
    """
    suite = __add_suite()  # 执行测试
    file_name = 'student_client.html'
    file = output_report.fileopen(path, file_name)
    runner = HTMLTestRunner_cn.HTMLTestRunner(
        stream=file,
        title=u'student_client',
        description=u'测试用例执行结果',
        verbosity=2,
        retry=2,
        save_last_try=False
    )
    result = runner.run(suite)
    result_format = get_report_data(file_name, result)
    ding_message_push(API['open_api'], file_name, result_format)
    file.close()
    return result_format


if __name__ == '__main__':
    run_suite('report/' + sys.argv[1] + '/html_report/')
