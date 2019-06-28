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
    "dubbing_recommendation": {
        'position': '//XCUIElementTypeStaticText[@name="配音推荐"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【配音推荐】',
        'input_character': ''
    },
    "dubbing_list": {
        'position': '//XCUIElementTypeStaticText[@name="配音达人榜"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【配音达人榜】',
        'input_character': ''
    },
    "my_voice": {
        'position': '//XCUIElementTypeStaticText[@name="我的配音"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【我的配音】',
        'input_character': ''
    },
    "read_picture_book": {
        'position': '//XCUIElementTypeStaticText[@name="已读绘本"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '点击【已读绘本】',
        'input_character': ''
    },
    "go_back1": {
        'position': '//XCUIElementTypeButton[@name="common icon back"]',
        'find_type': 'xpath',
        'operate_type': 'click',
        'operate_message': '返回上一级',
        'input_character': ''
    }
}
