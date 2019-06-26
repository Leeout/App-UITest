#!/usr/bin/env bash
echo "被测设备类型:"$1

echo "=================开始启动测试================="
python3 command_run.py -r $1

exit 0