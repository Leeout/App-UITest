"""
ios学生端主页-公开课 元素
"""

open_class = {
    "entrance": {
        'position': '//XCUIElementTypeStaticText[@name="公开课"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【公开课】',
        'input_character': ''
    },
    "go_back": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    }
}
