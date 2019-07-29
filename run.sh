#!/usr/bin/env bash
#启动说明（仅支持ios设备）
#参数$1:指定被测设备类型 如：ipad（学生端）|| iphone（家长端）
#参数$2:指定运行测试用例的次数 如：3

handle(){
# shellcheck disable=SC2078
if [[ ${1} == "ipad" || "iphone" ]]; then
    udid=$(idevice_id -l | head -n1)
    bundle_id=$(ideviceinstaller -l | grep WebDriverAgentRunner-Runner | awk 'BEGIN{ RS=","; } { print $0 }' | head -n1)
    if [[ ! (${udid} && ${bundle_id}) ]]; then
      echo "测试设备初始化失败,请检查设备连接或WebDriverAgentRunner是否正常安装！"
      exit 1
    fi
else
    echo "设备参数有误，请重新输入！"
    exit 1
fi
}

if handle "$1";then
    num=1
    while [[ ${num} -le $2 ]]
    do
        echo -e "\n第${num}次启动测试脚本......"
        python3 command_run.py -r "$1"
        (( num++ ))
    done
fi
