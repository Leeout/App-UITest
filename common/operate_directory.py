"""
该文件封装了对目录操作的方法
"""
import os

from common.time_base import get_today_date
from common.execute_command import execute_shell

get_file = os.path
path = get_file.dirname(get_file.realpath(__file__))  # 当前文件所在目录
yaml = get_file.join(path, "../report/html_report/")


def operate_directory(directory, command="mkdir"):
    """
    :param directory: 操作的路径
    :param command: 执行的命令
    :return: 返回执行命令获取的结果
    """
    complete_directory = directory + get_today_date() + '/'
    if os.path.exists(complete_directory) and command == "mkdir":
        return complete_directory
    else:
        execute_shell(command + " " + complete_directory)
        return complete_directory


if __name__ == '__main__':
    operate_directory(yaml)
