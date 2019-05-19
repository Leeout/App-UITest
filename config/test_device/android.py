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

platform_name = "Android"
app_activity = "com.dadaabc.zhuozan.dadaabcstudent.default"
app_package = "com.dadaabc.zhuozan.dadaabcstudent"
remote_appium_url = "http://192.168.132.232:4723/wd/hub"  # Linux服务器上的appium

android = {
    "huawei_mate9": {
        "platformName": platform_name,
        "platformVersion": "8.0.0",
        "deviceName": "HuaWei",
        "udid": "GWY0217824001505",
        "appActivity": app_activity,
        "appPackage": app_package,
        "remoteUrl": remote_appium_url
    }
}
