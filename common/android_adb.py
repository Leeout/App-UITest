"""
该文件封装了使用adb命令获取设备信息的方法
"""
import os


class AndroidAdb:
    def __setup_adb_server(self):
        # 启动adb server
        cmd = 'adb start-server'
        return os.popen(cmd)

    def get_device_id(self):
        self.__setup_adb_server()
        # 获取设备唯一标识符
        cmd = 'adb get-serialno'
        return os.popen(cmd)

    def get_device_model(self):
        # 获取设备型号，如：MHA-AL00
        cmd = 'adb shell getprop ro.product.model'
        return os.popen(cmd)

    def get_device_brand(self):
        # 获取设备品牌，如：HUAWEI
        cmd = 'adb shell getprop ro.product.brand'
        return os.popen(cmd)

    def get_platform_version(self):
        # 获取设备中的Android版本号，如4.2.2
        cmd = 'adb shell getprop ro.build.version.release'
        return os.popen(cmd)
