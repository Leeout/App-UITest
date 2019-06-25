"""组装设备信息"""
from selenium import webdriver

from common.logger import logger
from common.execute_command import execute_shell
from config.command.ios_libimobiledevice import IDEVICEINSTALLER


def __get_device_id():
    return execute_shell(IDEVICEINSTALLER['udid'])


# def __get_device_name():
#     return execute_shell(IDEVICEINSTALLER['device_name'] % __get_device_id())


def __get_device_version():
    return execute_shell(IDEVICEINSTALLER['product_version'] % __get_device_id())


def __get_bundle_id():
    return execute_shell(IDEVICEINSTALLER['bundle_id'])


def setup_ios_device():
    """
    参数解读：
    "autoAcceptAlerts": appium提供的自动关闭ios系统级弹窗参数
    "automationName": 使用的自动化测试引擎
    "platformName": 被测设备的平台
    "platformVersion": 被测设备的系统版本
    "deviceName":  被测设备的名称
    "udid": 被测设备的唯一标识符
    'app': 被测软件bundle_id 与android的包名同理,appium获取这个可以唤醒app
    "remoteUrl": appium server的地址
    """
    desired_caps = dict()
    desired_caps['autoAcceptAlerts'] = 'true'  # appium点击关闭权限弹窗
    desired_caps['automationName'] = "XCUITest"
    desired_caps['platformName'] = "ios"
    desired_caps['deviceName'] = "ios"
    desired_caps['udid'] = __get_device_id()
    desired_caps['app'] = __get_bundle_id()
    desired_caps['platformVersion'] = __get_device_version()
    test_device = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    logger.info('设备信息：%s', desired_caps)
    return test_device  # 接收指令的appium server端
