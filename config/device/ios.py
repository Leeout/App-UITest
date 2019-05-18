# -*- coding:utf-8 -*-
"""
存放被测ios设备的基本信息
"""
from logger import logger
from selenium import webdriver
from appium import webdriver

device = {
    "platformName": "ios",
    "platformVersion": "11.3",
    "automationName": "XCUITest",
    "deviceName": "iPhone 8 Plus",
    "udid": "cadefa3820d7e1f060a9651b022459672e46c9b0",  # ios设备的唯一标识符
    'app': 'com.dadaabc.DaDaClass',  # bundleId 与 androidPackage同理，appium获取这个可以唤醒app
    'autoAcceptAlerts': 'true',  # appium提供的自动关闭ios系统级弹窗参数
    "remoteUrl": "http://localhost:4723/wd/hub"
}


def device_info():
    """组装设备信息"""
    desired_caps = dict()
    desired_caps['platformName'] = device['platformName']  # 设置平台       
    desired_caps['platformVersion'] = device['platformVersion']  # 系统版本 
    desired_caps['automationName'] = device['automationName']
    desired_caps['deviceName'] = device['deviceName']
    desired_caps['udid'] = device['udid']  # 设备id ios机器唯一标识 
    desired_caps['app'] = device['app']
    desired_caps['autoAcceptAlerts'] = device['autoAcceptAlerts']  # appium点击关闭权限弹窗
    my_driver = webdriver.Remote(device['remoteUrl'], desired_caps)  # 接收指令的appium server端
    logger.info('设备信息：%s', desired_caps)
    return my_driver
