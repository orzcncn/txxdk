# txxdk
小程序UI自动化

## 框架选择

- python3 
- Uiautomator2
- pytest 
- allure

## 特性
- 纯正pageobject模式，复用性强
- 支持失败自动重试（提高稳定性）
- 支持无线运行
- 支持多机模式
- 参数化数据
- 失败自动截图

### 框架目录
Radiance测试框架目录
```
|--modules                               -----pageobject模块  
|   |--base.py                           -----测试基类,各个pageobject的基类
|   |--pagea.py                          -----页面实现
|   |--submodule
|       |--pageb.py
|--statics                               -----静态资源文件维护
|--testcases                             -----测试用例目录
|   |--testpagea.py                      -----pagea页面的测试类
|   |--submodule
|       |--testpageb.py 
|--tools
|   |--loggers.py                        -----日志处理模块
|   |--error.py                          -----错误处理模块
|config.py                               -----基础配置
|driver.py                               -----driver设置 初始化
|conftest.py                             -----pytest fixture配置
|run.py                                  -----生成报告方法
```

###使用
创建python3虚拟环境
Pycharm --file--setting--ProjectIncerpreter--add virtualenv
什么都不勾选    
导入项目到pycharm，选择新创建的virtualenv,按提示安装requirements文件

### 测试报告展示
![overview](https://github.com/orzcncn/txxdk/blob/master/static/overview.png)
![Categories](https://github.com/orzcncn/txxdk/blob/master/static/Categories.png)
![Behaviors](https://github.com/orzcncn/txxdk/blob/master/static/Behaviors.png)
![Graphs](https://github.com/orzcncn/txxdk/blob/master/static/Graphs.png)
![packages](https://github.com/orzcncn/txxdk/blob/master/static/packages.png)