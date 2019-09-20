#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-18 14:49
# @Author  : Innocence
# @Site    : 
# @File    : driver.py
# @Software: PyCharm

import uiautomator2 as ut2
from config import *
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Driver():
    def init_driver(self,device_name):
        """
        初始化driver 设置全局driver
        is_clear:清除数据
        :return:
        """
        try:
            logger.info(device_name)
            d = ut2.connect(device_name)
            # d = ut2.connect("172.21.17.51")
            # d.healthcheck()   # 自动唤醒设备
            # logger.info("设备信息:{}".format(d.info))
            # 设置全局寻找元素超时时间
            d.wait_timeout = wait_timeout  # default 20.0
            # 设置点击元素延迟时间
            d.click_post_delay = click_post_delay
            # d.service("uiautomator").stop()    # 停止uiautomator 可能和atx agent冲突
            logger.info("连接设备:{}".format(device_name))
            return d
        except Exception as e:
            logger.info("初始化driver异常!{}".format(e))
