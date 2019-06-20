"""
ios学生端主页-课后任务 元素
"""

after_class_tasks = {
    "entrance": {
        'position': '//XCUIElementTypeStaticText[@name="课后任务"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【课后任务】',
        'input_character': ''
    },
    "completed": {
        'position': '//XCUIElementTypeButton[@name="已完成"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【已完成】',
        'input_character': ''
    },
    "class_task": {
        'position': '//XCUIElementTypeButton[@name="随堂任务"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【随堂任务】',
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
