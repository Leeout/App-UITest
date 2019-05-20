# -*- coding:utf-8 -*-
"""
ios家长端学生登录涉及的元素
"""
login = {
    "click_login": {
        "position": '//XCUIElementTypeButton[@name="登录"]',
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击启动页【登录】按钮",
        "input_character": ""
    },
    "mobile": {
        "position": '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementType'
                    'Other[1]/XCUIElementTypeTextField',
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击手机输入框",
        "input_character": "15601754590"
    },
    "password": {
        "position": '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementType'
                    'Other[2]/XCUIElementTypeSecureTextField',
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击密码输入框",
        "input_character": "666666",
    },
    "confirm_login": {
        "position": '//XCUIElementTypeButton[@name="确定"]',
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击【确认登录】",
        "input_character": ""
    }
}
