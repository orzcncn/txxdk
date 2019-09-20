#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 13:53
# @Author  : Innocence
# @Site    : 
# @File    : xcx.py
# @Software: PyCharm

from module.base import Base
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

xxdk_xcx = "小熊家长会"

home_page = "首页"
discover_page = "发现"
mine_page = "我的"
tag = "历史班级"      # 用来标记小程序渲染完成，这样点击其它TAB不会回到首页


class Xcx(Base):
    def __init__(self, driver):
        self.base = Base(driver)
        self.base.wait_element_appear("发现", "微信发现")
        self.base.toast_show("初始化小程序", 3)
        self.base.wipe_down(0.1)
        self.base.click(xxdk_xcx, xxdk_xcx)

    def home_tab(self):            # 进入默认为首页
        self.base.wait_element_appear(tag, tag, timeout=10)
        self.base.toast_show("进入首页", 2)
        self.base.click_advance({"location": (0.161, 0.958), "description": "小程序首页"})

    def discover_tab(self):
        self.base.wait_element_appear(tag, tag, timeout=10)
        self.base.toast_show("进入发现页", 2)
        self.base.click_advance({"location": (0.497, 0.954), "description": "小程序发现页"})

    def mine_tab(self):
        self.base.wait_element_appear(tag, tag, timeout=10)
        self.base.toast_show("进入我的页", 2)
        self.base.click_advance({"location": (0.829, 0.958), "description": "小程序我的页"})
