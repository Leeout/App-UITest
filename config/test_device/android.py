# -*- coding:utf-8 -*-
"""
存放被测android设备的基本信息

参数解读：
"platformName": 被测设备的平台
"platformVersion": 被测设备的系统版本
"deviceName": 被测设备的名称
"udid": 被测设备的唯一标识符
"appActivity": 被测软件的activity页面
"appPackage": 被测软件包名,appium获取这个可以唤醒app
"remoteUrl": appium server的地址
"""
from common.execute_command import execute_shell
from config.command.android_adb import ADB

platform_name = "Android"
app_activity = "com.dadaabc.zhuozan.dadaabcstudent.default"
app_package = "com.dadaabc.zhuozan.dadaabcstudent"
remote_appium_url = "http://192.168.132.232:4723/wd/hub"  # Linux服务器上的appium

android = {
    execute_shell(ADB['device_brand']): {
        "platformName": platform_name,
        "platformVersion": execute_shell(ADB['platform_version']),
        "deviceName": execute_shell(ADB['device_model']),
        "udid": execute_shell(ADB['device_id']),
        "appActivity": app_activity,
        "appPackage": app_package,
        "remoteUrl": remote_appium_url
    }
}
