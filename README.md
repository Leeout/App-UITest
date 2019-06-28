#### 1.目录结构
>app                      存放被测app

>common                   公用方法

>config                   基础数据配置

>docs                     测试涉及文档

>report                   测试截图、报告存放

>testAndroid              测试 android机

>testIOS                  测试 ios机

>CHANGELOG.md             更新日志

>run.sh 启动测试的脚本


#### 2.appium server 环境安装
在 docs > environment 详细说明


#### 3.项目静态代码检查
pylint abc-qa-app-UITest --rcfile=pylint.conf

#### 其它
通过添加环境变量，解决python命令行调用问题

例如 vim ~/.zshrc :
export PYTHONPATH=$PYTHONPATH:/Users/chris/git/test/abc-qa-unittest:/Users/chris/git/test/abc-qa-unittest/venv/lib/python3.7/site-packages