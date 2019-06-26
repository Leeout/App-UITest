"""
ios学生端主页-我的课程 元素
"""

my_course = {
    "entrance": {
        'position': '//XCUIElementTypeStaticText[@name="我的课程"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【我的课程】',
        'input_character': ''
    },
    # "stage_learning_objectives": {
    #     'position': '//XCUIElementTypeStaticText[@name="Unit 1: Take a New Step"]',
    #     'find_type': 'xpath',
    #     'operate_type': 'click',
    #     'operate_message': '点击【阶段学习目标】观看视频',
    #     'input_character': ''
    # },
    # "go_back1": {
    #     'position': '//XCUIElementTypeButton[@name="common icon back"]',
    #     'find_type': 'xpath',
    #     'operate_type': 'click',
    #     'operate_message': '返回上一级',
    #     'input_character': ''
    # },
    "previous_courses": {
        'position': '//XCUIElementTypeApplication[@name="DaDa英语"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUI'
                    'ElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementType'
                    'Other[2]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【往期课程】',
        'input_character': ''
    },
    "swip_left": {
        'position': '',
        'find_type': '',
        'operate_type': 'swip',
        'operate_message': '向左滑动页面',
        'input_character': ''
    },
    "cancelled": {
        'position': '//XCUIElementTypeButton[@name="已取消"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【已取消】',
        'input_character': ''
    },
    "go_back2": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    },
    "go_back3": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回首页',
        'input_character': ''
    }
}
