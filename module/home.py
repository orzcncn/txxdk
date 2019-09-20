#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-19 09:46
# @Author  : Innocence
# @Site    : 
# @File    : home.py
# @Software: PyCharm


from module.xcx import Xcx
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


customer_ad = "关注公众号"
teacher_help = "教师指南"
parent_help = "家长指南"
vip_ad = {"location": (0.5, 0.376), "description": "首页会员广告"}
history_class = "历史班级"
new_class = "新建班级"
enter_common_class_element = "图"
enter_advance_class_element = "自动化高级班级"
manage = "管理"
home_help = {"location": (0.906, 0.789), "description": "首页帮助-跳转去吐个槽"}


class Home(Xcx):

    def __init__(self, driver):
        self.xcx = Xcx(driver)
        self.base = self.xcx.base

    def home_customer_ad(self):
        self.base.click(customer_ad, customer_ad)

    def home_teacher_guidelines(self):
        self.base.click(teacher_help, teacher_help)

    def home_parent_guidelines(self):
        self.base.click(parent_help,parent_help)

    def home_vip_ad(self):
        self.base.wait_element_appear(history_class, history_class)
        self.base.click_advance(vip_ad)

    def home_history_class(self):
        self.base.click(history_class,history_class)

    def home_enter_common_class(self):
        self.base.click(enter_common_class_element, enter_common_class_element)
        self.base.wait_element_appear("邀请打卡", "邀请打卡")

    def home_enter_advance_class(self):
        self.base.click(enter_advance_class_element, enter_advance_class_element)
        self.base.wait_element_appear("邀请打卡", "邀请打卡")

    def home_new_class(self):
        self.base.click(new_class, new_class)

    def home_help(self):
        self.base.click_advance(home_help)

    def home_delete_class(self):
        self.base.swipe_to_element(manage, history_class)




