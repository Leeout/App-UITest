# -*- coding:utf-8 -*-
from logger import logger
from selenium import webdriver

device = {
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "deviceName": "HuaWei",
    "udid": "emulator-5554",
    "appActivity": ".account.accountlogin.LoginActivity",
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
