"""
该文件封装了执行shell命令等方法
注：os.popen(command) 执行后只会输出内存的对象地址，所以需在后面调用readlines方法才能获取具体命令执行的结果
"""
import os

from common.logger import logger


def execute_shell(command):
    """
    :param command: 运行的命令
    :return: 去除\n等多余字符的str类型结果
    """
    try:
        result = os.popen(command).readlines()
        return ''.join(result).replace("\n", "")

    except Exception as error:
        logger.error('execute command fail:%s', error)
        return


if __name__ == '__main__':
    print(execute_shell("idevice_id -l"))
