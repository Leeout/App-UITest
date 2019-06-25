"""
本文件的作用是测试报告的输出，方便后面做持续集成时使用，目前test suite中没有使用
"""
from common.logger import logger
from common.time_base import get_current_time


def fileopen(path, name):
    """创建测试报告文件"""
    logger.debug('report path = %s', path)
    filename = path + get_current_time() + name
    file = open(filename, 'wb')
    return file
