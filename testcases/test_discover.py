#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 16:54
# @Author  : Innocence
# @Site    : 
# @File    : test_discover.py
# @Software: PyCharm

import pytest,time,allure
from module.discover import Discover
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

@allure.feature("测试发现")
@pytest.mark.usefixtures('driver_setup')
class TestDiscover:

    @pytest.fixture()
    def init(self, scope="class"):
        self.discover = Discover(self.driver)
        self.base = self.discover.base
        logger.info("初始化发现模块")
        yield self.discover
        logger.info("结束发现模块")

    @allure.story('测试发现课程')
    def test_discover_course(self, init):
        init.discover_course()
        if self.base.elements_exist("限时优惠"):
            self.base.assert_exist("限时优惠")
        else:
            self.base.assert_exist("查看关卡")

    @allure.story('测试发现课程图片进入')
    def test_discover_banner_course(self, init):
        init.discover_banner_course()
        if self.base.elements_exist("限时优惠"):
            self.base.assert_exist("限时优惠")
        else:
            self.base.assert_exist("查看关卡")
