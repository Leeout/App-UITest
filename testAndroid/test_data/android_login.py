# -*- coding:utf-8 -*-
"""
android家长端学生登录涉及的元素
"""
login = {
    "startup_page_click_login": {
        "position": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget."
                    "TextView[3]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击启动页登录按钮",
        "input_character": ""
    },
    "mobile": {
        "position": "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                    "android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view."
                    "ViewGroup[1]/android.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击手机号输入框",
        "input_character": "15601754590"
    },
    "password": {
        "position": "/hierarchy/Android.widget.FrameLayout/Android.widget.LinearLayout/Android.widget.FrameLayout/"
                    "Android.widget.LinearLayout/Android.widget.FrameLayout/Android.view.ViewGroup/Android"
                    ".view.ViewGroup[2]/Android.widget.EditText",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击密码输入框",
        "input_character": "754590"
    },
    "confirm_login": {
        "position": "/hierarchy/Android.widget.FrameLayout/Android.widget.LinearLayout/Android.widget.FrameLayout"
                    "/Android.widget.LinearLayout/Android.widget.FrameLayout/Android.view.ViewGroup/Android.widget."
                    "TextView[6]",
        "find_type": "xpath",
        "operate_type": "click",
        "operate_message": "点击登录按钮",
        "input_character": ""
    }
}

if __name__ == '__main__':
    print(login['startup_page_click_login'])
