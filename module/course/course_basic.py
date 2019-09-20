#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 16:31
# @Author  : Innocence
# @Site    : 
# @File    : course_basic.py
# @Software: PyCharm


from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


# todo 根据可以定位的元素 根据d(element).info 计算出相对位置 然后再根据坐标去点击计算 这样兼容性更强
customer_ad = "关注公众号"
punch_button = {"location": (0.507, 0.336), "description": "进入打卡"}
punch_calendar = "今天"
flower_list = {"location": (0.415, 0.4), "description": "老师收花列表"}
send_flow = "送花"
message = "消息"
charts = "排行榜"
share_button = "邀请打卡"
share_button_text = "分享"
more_setting = {"location": (0.924, 0.397), "description": "更多设置"}
notice = "公告"
filter = "筛选"
more_course = {"location": (0.911, 0.773), "description": "更多课程"}
navigate = "快捷"
comment = "评论"
praise = "赞"
diary_share = "分享"
already_punch = "已打卡"


class Coursebasic(Home):

    def __init__(self, driver):
        self.home = Home(driver)
        self.home.home_enter_common_class()
        self.base = self.home.xcx.base

    def enter_course(self, element):
        self.base.click(element, element)

    def course_basic_customer_ad(self):
        self.base.click(customer_ad, customer_ad)

    def course_basic_punch(self):
        self.base.click_advance(punch_button)

    def course_basic_flow_list(self):
        self.base.click_advance(flower_list)

    def course_basic_send_flow(self):
        self.base.click(send_flow, send_flow)

    def course_basic_message(self):
        self.base.click(message, message)

    def course_basic_charts(self):
        self.base.click(charts, charts)

    def course_basic_settings(self):
        self.base.click_advance(more_setting)

    def course_basic_share_button(self):
        self.base.click(share_button, share_button)

    def course_basic_filter(self):
        self.base.click(filter, filter)

    def course_basic_more_course(self):
        self.base.click_advance(more_course)

    def course_basic_navigate(self):
        self.base.click(navigate, navigate)

    def course_basic_comment(self):
        self.base.click(comment, comment)

    def course_basic_praise(self):
        self.base.click(praise, praise)

    def course_basic_diary_share(self):
        self.base.click(diary_share, diary_share)

    def course_basic_diary_view(self):
        self.base.click(already_punch, already_punch)
