# -*- coding:utf-8 -*-
"""
存放被测ios设备的基本信息

参数解读：
"automationName": 使用的自动化测试引擎
"platformName": 被测设备的平台
"platformVersion": 被测设备的系统版本
"deviceName":  被测设备的名称
"udid": 被测设备的唯一标识符
'app': 被测软件bundle_id 与android的包名同理,appium获取这个可以唤醒app
'autoAcceptAlerts': appium提供的自动关闭ios系统级弹窗参数
"remoteUrl": appium server的地址
"""

platform_name = "ios"
automation_name = "XCUITest"
app_bundle_id = 'com.dadaabc.DaDaClass'
handle_system_popup = 'true'
remote_appium_url = "http://localhost:4723/wd/hub"  # 本地的appium

ios = {
    "iphone_8p": {
        "automationName": automation_name,
        "platformName": platform_name,
        "platformVersion": "11.3",
        "deviceName": "iPhone 8 Plus",
        "udid": "cadefa3820d7e1f060a9651b022459672e46c9b0",
        'app': app_bundle_id,
        'autoAcceptAlerts': handle_system_popup,
        "remoteUrl": remote_appium_url
    }
}
