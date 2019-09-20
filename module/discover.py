#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 16:32
# @Author  : Innocence
# @Site    : 
# @File    : discover.py
# @Software: PyCharm

from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


racite_course = "五六年级古诗"
banner_course = "//android.widget.Image"
banner_course_text = "滚动海报图"

class Discover(Home):

    def __init__(self,driver):
        self.discover = Home(driver)
        self.discover.discover_tab()
        self.base = self.discover.base

    def discover_course(self):
        self.base.click(racite_course, racite_course)

    def discover_banner_course(self):
        self.base.click(banner_course, banner_course_text)

