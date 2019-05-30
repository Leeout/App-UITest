"""组装设备信息"""
from selenium import webdriver

from common.logger import logger
from common.execute_command import execute_shell
from config.test_device.android import android
from config.command.android_adb import ADB


def setup_android_device():
    execute_shell(ADB['setup_adb'])
    desired_caps = dict()
    for key in android:
        device = android[key]
        desired_caps['platformName'] = device['platformName']  # 设置平台       
        desired_caps['platformVersion'] = device['platformVersion']  # 系统版本       
        desired_caps['deviceName'] = device['deviceName']  # 设备id android机唯一标识   
        desired_caps['appPackage'] = device['appPackage']  # app包名      
        desired_caps['appActivity'] = device['appActivity']  # 启动的activity 
        my_driver = webdriver.Remote(device['remoteUrl'], desired_caps)  # 接收指令的appium server端
        logger.info('设备信息：%s', desired_caps)
        return my_driver
