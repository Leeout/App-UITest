"""
ios学生端主页-有声绘本 元素
"""

audio_picture_book = {
    "entrance": {
        'position': '//XCUIElementTypeStaticText[@name="有声绘本"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【有声绘本】',
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
