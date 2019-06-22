"""
ios家长端学生登录后的主页tab元素(涉及4个tab)
"""

home_page = {
    'appointment_course': {
        'position': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementType'
                    'TabBar[1]/XCUIElementTypeButton[2]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '主页：【约课】',
        'input_character': ''
    }
}