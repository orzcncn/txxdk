#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 15:35
# @Author  : Innocence
# @Site    : 
# @File    : course_advance.py
# @Software: PyCharm
from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()



share_button_text = "分享"
assign_homework = "发布今日学习主题"

class Courseadvance(Home):

    def __init__(self, driver):
        self.home = Home(driver)
        self.home.home_enter_class()
        self.base = self.home.xcx.base

    def course_advance_assign_homework(self):
        self.base.click(assign_homework, assign_homework)

    def course_advance_share(self):
        self.base.click(share_button_text, share_button_text)







