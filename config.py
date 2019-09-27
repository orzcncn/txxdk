#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-18 14:50
# @Author  : Innocence
# @Site    : 
# @File    : config.py
# @Software: PyCharm

import os

# 全局配置
pck_name = "com.tencent.mm"   # 包名
device_name = "79URX19227000484"  #设备名
wait_timeout = 20
click_post_delay = 1
launch_time = 4
current_path = os.path.abspath(os.path.dirname(__file__))
screenshots_folder = os.path.join(current_path, "screenshots")
if not os.path.exists(screenshots_folder):
    os.mkdir(screenshots_folder)
    print("创建截图目录:{}".format(screenshots_folder))
