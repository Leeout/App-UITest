"""
ios家长端启动页的元素
"""
start_page = {
    "click_debug_popup": {
        'position': '//XCUIElementTypeButton[@name="确定"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '家长端app启动页debug弹窗',
        'input_character': ''
    }
    # "skip": {
    #     'position': '//XCUIElementTypeButton[@name="跳过"]',
    #     'find_type': 'xpath',
    #     'operate_type': 'click',
    #     'operate_message': '家长端app启动页右上角【跳过】按钮',
    #     'input_character': ''
    # }
    # "experience_now": {
    #     'position': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementType'
    #                 'Other[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElement'
    #                 'TypeOther[1]/XCUIElementTypeButton[1]',
    #     'find_type': 'xpath',
    #     'operate_type': 'click',
    #     'operate_message': '点击启动页：【立即体验】',
    #     'input_character': ''
    # }
}
