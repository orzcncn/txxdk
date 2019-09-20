#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-20 21:33
# @Author  : Innocence
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm

import subprocess, pytest, time, allure
import base64
from driver import Driver
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.fixture()
def driver_setup(request):
    logger.info("自动化测试开始!")
    request.instance.driver = Driver().init_driver(device_name)
    logger.info("driver初始化")
    request.instance.driver.app_start(pck_name, stop=True)
    time.sleep(launch_time)
    allow(request.instance.driver)
    
    def driver_teardown():
        logger.info("自动化测试结束!")
        request.instance.driver.app_stop(pck_name)
    request.addfinalizer(driver_teardown)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    hook pytest失败
    :param item:
    :param call:
    :return:
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        pic_info = adb_screen_shot()
        with allure.step('添加失败截图...'):
            allure.attach.file( pic_info, "失败截图", attachment_type=allure.attachment_type.PNG)


def allow(driver):
    """
    监听一些跳过和确定
    :param driver:
    :return: 
    """
    driver.watcher("知道了 ").when(text="知道了 ").click(text="知道了 ")
    driver.watcher("允许").when(text="允许").click(text="允许")
    driver.watcher("跳过").when(text="跳过").click(text="跳过")
    driver.watcher("不要啦").when(text="不要啦").click(text="不要啦")


def screen_shot(driver):
    """
    截图操作
    pic_name:截图名称
    :return:
    """
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshots_folder, fail_pic)
        driver.screenshot("{}.png".format(pic_name))
        logger.info('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        logger.info("{}截图失败!{}".format(pic_name, e))


def adb_screen_shot():
    """
    adb截图
    :return:
    """
    file_info = ''
    fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fail_pic = str(fail_time) + "截图.jpg"
    pic_name = os.path.join(screenshots_folder, fail_pic)
    cmd = 'adb shell /system/bin/screencap -p /sdcard/screenshot.jpg'
    subprocess.call(cmd,shell=True)
    cmd = 'adb pull /sdcard/screenshot.jpg {}'.format(pic_name)
    subprocess.call(cmd, shell=True)
    # with open(pic_name, 'rb') as r:
    #     file_info = r.read()
    # return file_info
    return pic_name




