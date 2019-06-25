#!/usr/bin/env bash
#该文件用来启动测试（传参为运行设备类型简称）
#work_dir=$(cd $(dirname $0); pwd)
#echo "测试工程目录："${work_dir}
#export PYTHONPATH=${PYTHONPATH}:${work_dir}:${work_dir}/venv/lib/python3.6/site-packages
#echo "python运行环境配置："${PYTHONPATH}

echo "被测设备类型:"$1
python3 command_run.py -r $1

exit 0