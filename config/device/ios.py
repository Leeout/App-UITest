# -*- coding:utf-8 -*-
"""
存放被测ios设备的基本信息
"""
from logger import logger
from selenium import webdriver
from appium import webdriver

device = {
    "platformName": "ios",
    "platformVersion": "12.2",
    "deviceName": "iPhone Xʀ",  # xcode ios模拟器
    "uuid": "4CBB6C28-67C2-4ED5-B357-80B5D7B905B8",  # ios模拟器的唯一标识符
    # 'app': '/Users/lijie/Desktop/DaDaClass(1).app',  # 安装app的路径
    'app': 'com.dadaabc.DaDaClass',  # bundle id 与 android appPackage同理，appium获取这个可以唤醒app
    'autoAcceptAlerts': 'true',  # appium提供的自动关闭ios系统级弹窗参数
    "remoteUrl": "http://localhost:4723/wd/hub"
}


def device_info():
    """组装设备信息"""
    desired_caps = dict()
    desired_caps['app'] = device['app']
    desired_caps['platformName'] = device['platformName']  # 设置平台       
    desired_caps['platformVersion'] = device['platformVersion']  # 系统版本       
    desired_caps['deviceName'] = device['deviceName']  # 设备id ios机器唯一标识 
    desired_caps['autoAcceptAlerts'] = device['autoAcceptAlerts']  # appium点击关闭权限弹窗
    my_driver = webdriver.Remote(device['remoteUrl'], desired_caps)  # 接收指令的appium server端
    logger.info('设备信息：%s', desired_caps)
    return my_driver
