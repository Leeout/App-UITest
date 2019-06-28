"""
ios学生端主页-百宝箱 元素
"""

baibao_box = {
    "entrance": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementType'
                    'Other[5]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【百宝箱】',
        'input_character': ''
    },
    "go_back": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回首页',
        'input_character': ''
    }
}