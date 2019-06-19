"""
ios学生端登录元素
"""

login = {
    "mobile": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElement'
                    'TypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击手机输入框',
        'input_character': '15601754590'
    },
    "password": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElement'
                    'TypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeSecureTextField',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击密码输入框',
        'input_character': '754590'
    },
    "confirm_login": {
        'position': '//XCUIElementTypeButton[@name="登录"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【登录】',
        'input_character': ''
    }
}
