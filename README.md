### 1、appium server 环境安装

在 docs > appium_environment 有详细说明


### 2、项目静态代码检查

pylint abc-qa-app-UITest --rcfile=pylint.conf


### 其它

通过添加环境变量，解决python命令行调用问题

例如 vim ~/.zshrc :
export PYTHONPATH=$PYTHONPATH:/Users/chris/git/test/abc-qa-unittest:/Users/chris/git/test/abc-qa-unittest/venv/lib/python3.7/site-packages

