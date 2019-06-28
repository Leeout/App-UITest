"""
ios学生端 【有声绘本】的用例
"""
from common.logger import logger
from common.operate_element import main_operate

from testIOS.element.student_client.login import login
from testIOS.element.student_client.audio_picture_book import audio_picture_book


def __case_collection(driver, platform):
    # operate_element(driver, platform, **login)
    main_operate(driver, platform, **audio_picture_book)


def enter_audio_picture_book(driver):
    logger.warning('测试开始......')
    __case_collection(driver, 'ipad')
    logger.warning('测试结束......')
