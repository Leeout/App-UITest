"""组装设备信息"""
from common.logger import logger
from selenium import webdriver
from config.test_device.ios import ios


def setup_ios_device():
    desired_caps = dict()
    for key in ios:
        device = ios[key]
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
