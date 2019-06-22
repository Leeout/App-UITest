"""
该文件是获取各种格式时间的一系列方法封装
"""
import datetime


def get_current_time():
    """获取当前时间 年月日格式"""
    return str(datetime.datetime.now())


if __name__ == '__main__':
    get_current_time()
