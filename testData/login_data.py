# -*- coding:utf-8 -*-
"""
家长端学生登录涉及的元素
"""
login = {
    "mobile": {
        "position": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                    "FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup" \
                    "/android.view.ViewGroup[1]/android.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击手机号输入框",
        "input_character": "15601754590"
    },
    "password": {
        "position": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                    ".view.ViewGroup[2]/android.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击密码输入框",
        "input_character": "754590"
    },
    "confirm_login": {
        "position": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                    ".TextView[6]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击登录按钮",
        "input_character": ""
    }
}

if __name__ == '__main__':
    print login['mobile']
