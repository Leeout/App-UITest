### 写在前面
1.考虑到上海QA团队成员的实际情况，决定从0到1实现APP UI自动化测试框架

#### 目录结构：
├── CHANGELOG.md             更新日志
├── README.md                使用说明
├── common                   公用方法
│   ├── logger.py            日志方法
│   ├── operate_element.py   操作元素
│   └── time_base.py         获取时间戳
├── config                   基础数据
│   └── device.py            测试设备信息
├── start_test.py            启动运行测试
├── testAndroid              android机测试
│   ├── test_case
│   │   └── test01_student_login.py
│   ├── test_data
│   │   ├── home_page.py
│   │   └── login_data.py
│   └── test_report
│       └── error_screenshot
└── testIOS                  ios机测试
    ├── test_case.py
    ├── test_data.py
    └── test_report.py