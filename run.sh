#!/usr/bin/env bash
#启动说明（仅支持ios设备）
#参数$1:指定被测设备类型 如：ipad（学生端）|| parent（家长端）|| teacher（老师端）
#参数$2:指定运行测试用例的次数 如：3
udid=$(idevice_id -l | head -n1)

start_up_appium() {
  process=$(lsof -i:4723)
  if [[ ! ${process} ]]; then
    nohup appium -a 127.0.0.1 -p 4723 1>appium.log 2>&1
    return 0
  else
    echo "appium server进程正在运行中！"
    return 0
  fi
}

install_WebDriverAgent() {
  password="1234"
  security unlock-keychain -p $password ~/Library/Keychains/login.keychain
  nohup xcodebuild -project /Users/jason.lik/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$udid" test 1>appium.log 2>&1
  return 0
}

handle() {
  start_up_appium &
  #install_WebDriverAgent &
  if [[ ${1} == "ipad" || "parent" || "teacher" ]]; then
    bundle_id=$(ideviceinstaller -l | grep WebDriverAgentRunner-Runner | awk 'BEGIN{ RS=","; } { print $0 }' | head -n1)
    if [[ ! (${udid} && ${bundle_id}) ]]; then
      echo "测试设备初始化失败,请检查设备连接或WebDriverAgent是否正常安装！"
      exit 1
    fi
  else
    echo "设备参数有误，请重新输入！"
    exit 1
  fi
}

if handle "$1"; then
  sleep 5
  num=1
  while [[ ${num} -le $2 ]]; do
    echo -e "\n启动测试脚本-第${num}次......"
    case $1 in
    ipad)
      python3 testIOS/student_client/test_student_client.py "$1"
      ((num++))
      ;;
    parent)
      echo "test parent"
      ((num++))
      ;;
    teacher)
      echo "test teacher"
      ((num++))
      ;;
    esac
  done
fi
