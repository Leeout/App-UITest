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
    "into_webview": {
        'position': 1,
        'find_type': '',
        'operate_type': 'webview',
        'operate_message': '切换到H5【随堂任务】页面',
        'input_character': ''
    },
    "to_be_completed": {
        'position': '//XCUIElementTypeStaticText[@name="待完成"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【待完成】',
        'input_character': ''
    },
    "submitted": {
        'position': '//XCUIElementTypeStaticText[@name="已提交"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【已提交】',
        'input_character': ''
    },
    "view_details": {
        'position': '(//XCUIElementTypeStaticText[@name="查看详情"])[1]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击第一条任务的【查看详情】',
        'input_character': ''
    },
    "go_back1": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    },
    "comments": {
        'position': '//XCUIElementTypeStaticText[@name="已点评"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【已点评】',
        'input_character': ''
    },
    "back_native": {
        'position': 0,
        'find_type': '',
        'operate_type': 'webview',
        'operate_message': '退出H5【随堂任务】页面',
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
        'operate_message': '返回上一级',
        'input_character': ''
    }
}
