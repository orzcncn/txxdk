#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 14:56
# @Author  : Innocence
# @Site    : 
# @File    : course_editor.py
# @Software: PyCharm



from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

enter_classname_element = "请输入班级名称"
course_title = "班级名称"
class_name = "U2测试班级"
adult_type = "成人打卡"
child_type = "孩子学习打卡"
yw = "语文"
sx = "数学"
yy = "英语"
ty = "体育"
user_define_tag = "自定义"
enter_course_tag_element = "请输入自定义班级标签"
course_tag = "计算机"
course_tag_confirm = "确认"
next_step = "下一步 "
edit_title_page = "修改封面"
create_button = "创建"


class Courseeditor(Home):
    def __init__(self, driver):
        self.home = Home(driver)
        self.home.home_new_class()
        self.base = self.home.xcx.base

    def input_classname(self):
        self.base.wait_element_appear(course_title,course_title)
        self.base.send_keys(enter_classname_element, class_name, class_name)
        self.base.back()

    def select_coursetype(self, type_element):
        self.base.wait_element_appear(type_element,type_element)
        self.base.click(type_element, type_element)

    def select_subjectype(self, type_element):
        self.base.wait_element_appear(type_element,type_element)
        self.base.click(type_element, type_element)

    def select_subjecttype_user_define(self, user_define_tag):
        self.base.click(user_define_tag, user_define_tag)
        self.base.send_keys(enter_course_tag_element, course_tag, course_tag)
        self.base.back()

    def next_step(self):
        self.base.wait_element_appear(next_step, next_step)
        self.base.click(next_step, next_step)

    def create_course(self):
        self.base.wait_element_appear(edit_title_page, edit_title_page)
        self.base.wipe_up()
        self.base.click(create_button, create_button)


