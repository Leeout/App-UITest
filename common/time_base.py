"""
该文件是获取各种格式时间的一系列方法封装
"""
import time
import datetime


def get_current_time():
    """获取当前时间点 年-月-日 时:分:秒 格式"""
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_today_date():
    """获取今天日期 年-月-日 格式"""
    return str(datetime.date.today())


if __name__ == '__main__':
    # get_today_date()
    get_current_time()