"""
ios学生端主页-外教直播 元素
"""

teacher_live_broadcast = {
    "entrance": {
        'position': '//XCUIElementTypeStaticText[@name="外教直播"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【外教直播】',
        'input_character': ''
    },
    "swip_left1": {
        'position': '',
        'find_type': '',
        'operate_type': 'swip',
        'operate_message': '向左滑动页面',
        'input_character': ''
    },
    "previous_live_broadcasts": {
        'position': '//XCUIElementTypeApplication[@name="XXXX"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElement'
                    'TypeOther[2]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【往期直播】',
        'input_character': ''
    },
    "swip_left2": {
        'position': '',
        'find_type': '',
        'operate_type': 'swip',
        'operate_message': '向左滑动页面',
        'input_character': ''
    },
    "go_back1": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    },
    "go_back2": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    }
}
