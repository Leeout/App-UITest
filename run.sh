#!/usr/bin/env bash
#该文件用来启动测试（传参为运行设备类型简称）

case $1 in
    ios)
    python3 testIOS/start_test_ios.py
    ;;
    ipad)
    python3 testIOS/start_test_ipad.py
    ;;
    and | android)
    python3 testAndroid/start_test_android.py
    ;;
esac
