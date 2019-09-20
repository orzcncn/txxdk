#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-26 10:06
# @Author  : Innocence
# @Site    : 
# @File    : test_mine.py
# @Software: PyCharm

import pytest,allure
from module.mine import Mine
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@allure.feature("测试我的")
@pytest.mark.usefixtures('driver_setup')
class TestMine:

    @pytest.fixture()
    def init_mine(self, scope="class"):
        self.mine = Mine(self.driver)
        self.base = self.mine.base
        logger.info("初始化我的模块")
        yield self.mine
        logger.info("结束我的模块")

    @allure.story("我的账户")
    def test_mine_balance(self, init_mine):
        init_mine.mine_balance()
        init_mine.mine_diamont_pay()
        self.base.assert_exist("请输入支付密码")

    @allure.story("会员权益")
    def test_mine_rights(self, init_mine):
        init_mine.mine_rights("专属花朵")
        self.base.assert_exist("会员定制花朵 任性送老师")
        self.base.click("✖", "✖")
        # TODO 写法有点丑 后续封装下
        # init_mine.mine_rights("AI评测")
        # self.base.assert_exist("孩子的专属智能 陪伴小助手")
        # self.base.click("✖", "✖")
        # init_mine.mine_rights("专属皮肤")
        # self.base.assert_exist("会员标识及皮肤 彰显与众不同")
        # self.base.click("✖", "✖")
        # init_mine.mine_rights("优惠入班")
        # self.base.assert_exist("会员购买打卡课程 可享受专属折扣")
        # self.base.click("✖", "✖")
        # init_mine.mine_rights("记录下载")
        # self.base.assert_exist("学习打卡记录 随时下载")
    
    @allure.story("我的评论")
    def test_mine_comment(self, init_mine):
        init_mine.mine_notebook()
        init_mine.mine_comment()
        self.base.assert_exist("这是评论")

    @allure.story("我的赞")
    def test_mine_priaise(self, init_mine):
        init_mine.mine_notebook()
        init_mine.mine_priaise()
        self.base.assert_exist("图为证")

    @allure.story("日记本")
    def test_mine_notebook(self, init_mine):
        init_mine.mine_notebook()
        self.base.click("群名：图", "群名：图")
        self.base.assert_exist("2019.04.08")

    @allure.story("优惠券")
    def test_mine_coupon(self, init_mine):
        init_mine.mine_coupon()
        self.base.click("立刻使用", "立刻使用")
        self.base.assert_exist("家庭教育收费班级")

    @allure.story("我的-礼物兑换")
    def test_mine_gift(self, init_mine):
        init_mine.mine_gift()
        self.base.assert_exist("礼物兑换")

    @allure.story("我的-排行榜")
    @pytest.mark.parametrize("_type", ["积分榜", "鲜花榜", "勋章榜"])
    def test_mine_chart(self, init_mine, _type):
        init_mine.mine_chart()
        self.base.assert_exist("第1名")
        self.base.assert_exist("一年级一班")
        self.base.click(_type, _type)
        if _type == "积分榜":
            self.base.assert_exist("实验三小2018级3班")
        else:
            self.base.assert_exist("Linda")

    @allure.story("我的-分享小程序")
    def test_mine_share(self, init_mine):
        init_mine.mine_share()
        self.base.assert_exist("创建新聊天")

    @allure.story("我的-帮助")
    def test_mine_help(self, init_mine):
        init_mine.mine_help()
        self.base.assert_exist("吐个槽社区")
