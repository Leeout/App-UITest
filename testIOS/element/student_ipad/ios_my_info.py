"""
ios学生端主页-头部 可点击的按钮元素组合
"""

my_info = {
    "user_avatar": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementType'
                    'Other[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击左上角用户头像',
        'input_character': ''
    },
    "test_report": {
        'position': '//XCUIElementTypeStaticText[@name="测试报告"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【测试报告】',
        'input_character': ''
    },
    "close_myinfo_window": {
        'position': '//XCUIElementTypeButton[@name="treasure cancel"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击窗口右上角【X】',
        'input_character': ''
    },
    "medal_wall": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/'
                    'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                    'TypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementType'
                    'Other',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【勋章墙】',
        'input_character': ''
    },
    "go_back": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击左上角【<】',
        'input_character': ''
    },


}
