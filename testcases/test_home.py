#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-20 21:30
# @Author  : Innocence
# @Site    : 
# @File    : test_home.py
# @Software: PyCharm

import pytest, allure
from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@allure.feature("测试首页")
class TestHome:

    @pytest.fixture()
    def init_home(self, scope="class"):
        self.home = Home(self.driver)
        logger.info("初始化首页模块")
        self.base = self.home.base
        yield self.home
        logger.info("结束首页模块")

    @allure.story("客服引导公众号关注")
    def test_home_customer_ad(self, init_home):
        init_home.home_customer_ad()
        self.base.assert_exist("客服会话")

    @allure.story('测试教师指南')
    def test_home_teacher_guidelines(self, init_home):
        init_home.home_teacher_guidelines()
        # self.base.assert_exist("教师指南")  纯图 无法判定

    @pytest.mark.flaky(reruns=5, reruns_delay=2)        # 重试机制
    @allure.story('测试家长指南')
    def test_home_parent_guidelines(self, init_home):
        init_home.home_parent_guidelines()
        # self.base.assert_exist("家长指南")  纯图 无法判定

    @allure.story("测试首页会员模块")
    def test_home_vip(self, init_home):
        init_home.home_vip_ad()
        self.base.assert_exist("限时优惠")

    @pytest.mark.run(order=2)                           # 设置用例执行顺序
    @allure.story('测试历史班级')
    def test_home_history_class(self, init_home):
        init_home.home_history_class()
        self.base.assert_exist("U2测试班级")

    @pytest.mark.P0                                     # 设置用例运行级别
    @allure.story('测试进入班级')
    def test_home_enter_class(self, init_home):
        init_home.home_enter_common_class()
        self.base.assert_exist("邀请打卡")

    @pytest.mark.run(order=1)                           # 设置用例执行顺序
    @allure.story("测试进入新建班级")
    def test_home_new_class(self, init_home):
        init_home.home_new_class()
        self.base.assert_exist("成人打卡")

    @allure.story("测试首页帮助进入吐个槽")
    def test_home_help(self, init_home):
        self.base.wait_element_appear("历史班级", "历史班级")
        init_home.home_help()
        self.base.assert_exist("吐个槽社区")

    @allure.story("测试删除班级")
    def test_home_delete_class(self, init_home):
        init_home.home_delete_class()
        self.base.assert_exist("U2测试班级")
        self.base.click("删除", "删除")
        self.base.click("确认", "确认")
        self.base.assert_not_exist("U2测试班级")


    # demo 用于查看allure feature,story,step的区别
    # @allure.story('步骤测试story0')
    # def test_abc1(self):
    #     assert 1==1
    #
    #
    # @allure.story('步骤测试story')
    # @allure.step("步骤测试step1")
    # def test_abc2(self):
    #     assert 1==1
    #
    #
    # @allure.story('步骤测试story')
    # @allure.step("步骤测试step2")
    # def test_abc(self):
    #     assert 1==1
    #
    #
    # @allure.step("步骤测试step3")
    # def test_abc4(self):
    #     assert 1==1