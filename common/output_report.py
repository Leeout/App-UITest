"""
该文件的作用是测试报告的输出
"""
from common.logger import logger
from common.time_base import get_current_hour_minute


def fileopen(path, name):
    """创建测试报告文件"""
    logger.debug('report path = %s', path)
    filename = path + get_current_hour_minute() + '__' + name
    file = open(filename, 'wb')
    return file
