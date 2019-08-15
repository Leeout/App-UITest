# -*- coding: utf-8 -*-
"""
存放ios libimobiledevice命令
"""

IDEVICEINSTALLER = {
    'device_name': 'ideviceinfo -u %s -k DeviceName',
    'product_version': 'ideviceinfo -u %s -k ProductVersion',
    'udid': 'idevice_id -l',
    'bundle_id': "ideviceinstaller -l | grep XXXX | awk 'BEGIN{RS = \", \";} {print $1}' | head -1"
}
