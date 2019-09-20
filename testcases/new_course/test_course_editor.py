#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 11:07
# @Author  : Innocence
# @Site    : 
# @File    : test_course_editor.py
# @Software: PyCharm

import allure, pytest
from module.new_course.course_editor import Courseeditor
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.feature("测试首页")
class Testcourseeditor:

    @pytest.fixture()
    def init_new_course(self, scope="class"):
        self.base = Courseeditor(self.driver)
        logger.info("初始化新建班级模块")
        yield self.base
        logger.info("结束新建班级模块")

    @pytest.mark.run(order=1)
    @allure.story("测试新建班级")
    def test_new_course(self, init_new_course):
        init_new_course.input_classname()
        init_new_course.select_coursetype("孩子学习打卡")
        init_new_course.select_subjectype("语文")
        init_new_course.next_step()
        init_new_course.create_course()
        init_new_course.base.assert_exist("立即邀请家长 ")

