"""
该文件封装了执行shell命令等方法
"""
import os


def execute_shell(command):
    return os.popen(command)
