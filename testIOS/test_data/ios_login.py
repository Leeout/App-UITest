# -*- coding:utf-8 -*-
"""
ios家长端学生登录涉及的元素
"""
login = {
    # "choose_password_login": {
    #     "position": "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementType"
    #                 "Other[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeButton[2]",
    #     "find_type": "xpath",
    #     "operate_type": "click",
    #     "operate_message": "点击【约课】页右上角的密码登录按钮",
    #     "input_character": ""
    # },
    "mobile": {
        "position": "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementType"
                    "Other[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementType"
                    "Other[1]/XCUIElementTypeTextField[1]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击手机输入框",
        "input_character": "15601754590"
    },
    "password": {
        "position": "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementType"
                    "Other[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementType"
                    "Other[2]/XCUIElementTypeSecureTextField[1]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击密码输入框",
        "input_character": "754590",
    },
    "confirm_login": {
        "position": "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementType"
                    "Other[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementType"
                    "Button[1]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "确认登录",
        "input_character": ""
    }
}
