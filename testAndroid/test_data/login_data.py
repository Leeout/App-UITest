# -*- coding:utf-8 -*-
"""
家长端学生登录涉及的元素
"""
login = {
    "mobile": {
        "position": "/hierarchy/testAndroid.widget.FrameLayout/testAndroid.widget.LinearLayout/testAndroid.widget." \
                    "FrameLayout/testAndroid.widget.LinearLayout/testAndroid.widget.FrameLayout/testAndroid.view.ViewGroup" \
                    "/testAndroid.view.ViewGroup[1]/testAndroid.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击手机号输入框",
        "input_character": "15601754590"
    },
    "password": {
        "position": "/hierarchy/testAndroid.widget.FrameLayout/testAndroid.widget.LinearLayout/testAndroid.widget" \
                    ".FrameLayout/testAndroid.widget.LinearLayout/testAndroid.widget.FrameLayout/testAndroid.view.ViewGroup/testAndroid"
                    ".view.ViewGroup[2]/testAndroid.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击密码输入框",
        "input_character": "754590"
    },
    "confirm_login": {
        "position": "/hierarchy/testAndroid.widget.FrameLayout/testAndroid.widget.LinearLayout/testAndroid.widget.FrameLayout" \
                    "/testAndroid.widget.LinearLayout/testAndroid.widget.FrameLayout/testAndroid.view.ViewGroup/testAndroid.widget"
                    ".TextView[6]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击登录按钮",
        "input_character": ""
    }
}

if __name__ == '__main__':
    print login['mobile']
