### 1、目录结构

├── Pipfile
├── Pipfile.lock
├── README.md
├── app
├── command_run.py
├── common
├── config
├── docs
├── pylint.conf
├── report
├── run.sh
├── testAndroid
├── testIOS
├── utils
└── venv

### 2、appium server 环境安装

在 docs > appium_environment 有详细说明


### 3、项目静态代码检查

pylint abc-qa-app-UITest --rcfile=pylint.conf


### 4、其它

通过添加环境变量，解决python命令行调用问题

例如 vim ~/.zshrc :
export PYTHONPATH=$PYTHONPATH:/Users/chris/git/test/abc-qa-unittest:/Users/chris/git/test/abc-qa-unittest/venv/lib/python3.7/site-packages

