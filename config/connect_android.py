"""组装设备信息"""
from selenium import webdriver
from appium import webdriver

from common.logger import logger
from common.execute_command import execute_shell
from config.command.android_adb import ADB


def __get_device_id():
    return execute_shell(ADB['device_id'])


def __get_device_name():
    return execute_shell(ADB['device_brand'])


def __get_device_version():
    return execute_shell(ADB['platform_version'])


def setup_android_device():
    try:
        desired_caps = dict()
        desired_caps['appPackage'] = "com.dadaabc.zhuozan.dadaabcstudent"  # app包名      
        desired_caps['appActivity'] = "com.dadaabc.zhuozan.dadaabcstudent.default"  # 启动的activity 
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = __get_device_version()
        desired_caps['deviceName'] = __get_device_name()
        desired_caps['udid'] = __get_device_id()
        logger.info('设备信息：%s', desired_caps)
        return webdriver.Remote("http://192.168.132.232:4723/wd/hub", desired_caps)  # 接收指令的appium server端

    except Exception as error:
        logger.error("setup android device fail:%s", error)
        return False
