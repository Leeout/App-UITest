#!/usr/bin/env bash
#启动说明
#参数$1:指定被测设备类型 如：ipad || iphone || android
#参数$2:指定运行测试用例的次数 如：3

get_WebDriverAgentRunner(){
bundle_id=$(ideviceinstaller -l | grep WebDriverAgentRunner-Runner | awk 'BEGIN{ RS=","; } { print $0 }' | head -n1)
if [[ ${bundle_id} == "com.apple.test.WebDriverAgentRunner-Runner" ]]; then
    return 0
else
    return 1
fi
}

init_device(){
if [[ ${1} == "ipad" || "iphone" ]]; then
    func=$(get_WebDriverAgentRunner)
    if [[ ${func} -ne 0 ]]; then
        password="1234"
        security unlock-keychain -p $password ~/Library/Keychains/login.keychain
        udid=$(idevice_id -l | head -n1)
        echo "开始build WebDriverAgent......"
        xcodebuild -project /Users/jason.lik/WebDriverAgent/WebDriverAgent.xcodeproj  -scheme WebDriverAgentRunner -destination "id=$udid" test
        echo "build WebDriverAgent完成"
        return $?
    else
        return 0
    fi
else
    echo "开始启动android adb服务......"
    adb start-server
    return $?
fi
}

if init_device "$1";then
    num=1
    while [[ ${num} -le $2 ]]
    do
        echo -e "\n第${num}次启动测试脚本......"
        python3 command_run.py -r "$1"
        (( num++ ))
    done
else
    echo "初始化设备环境失败，请手动build WebDriverAgentRunner!"
    exit 1
fi
