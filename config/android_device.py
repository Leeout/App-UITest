# -*- coding:utf-8 -*-
"""
存放被测android设备的基本信息
"""
from logger import logger
from selenium import webdriver

device = {
    "platformName": "Android",
    "platformVersion": "8.0.0",
    "deviceName": "HuaWei",
    "udid": "GWY0217824001505",  # 华为mate9
    "appActivity": "com.dadaabc.zhuozan.dadaabcstudent.default",
    "appPackage": "com.dadaabc.zhuozan.dadaabcstudent",
    "remoteUrl": "http://localhost:4723/wd/hub"
}


def device_info():
    desired_caps = dict()
    desired_caps['platformName'] = device['platformName']  # 设置平台       
    desired_caps['platformVersion'] = device['platformVersion']  # 系统版本       
    desired_caps['deviceName'] = device['deviceName']  # 设备id 安卓机唯一标识   
    desired_caps['appPackage'] = device['appPackage']  # app包名      
    desired_caps['appActivity'] = device['appActivity']  # 启动的activity 
    my_driver = webdriver.Remote(device['remoteUrl'], desired_caps)  # 接收指令的appium server端
    logger.info('设备信息：%s', desired_caps)
    return my_driver
