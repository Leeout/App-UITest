"""
存放android adb命令
"""

ADB = {
    'setup_adb': 'adb start-server',
    'device_id': 'adb get-serialno',
    'device_model': 'adb shell getprop ro.product.model',
    'device_brand': 'adb shell getprop ro.product.brand',
    'platform_version': 'adb shell getprop ro.build.version.release'
}
