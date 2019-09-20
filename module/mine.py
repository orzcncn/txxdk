#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-26 10:06
# @Author  : Innocence
# @Site    : 
# @File    : mine.py
# @Software: PyCharm

from module.home import Home
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()

# 会员模块
balance = "钻石余额 >"
diamont_pay = "微信支付￥0.01"
pay_tag = "请输入支付密码"
account_num = "编号:619151"
vip_time = "会员有效期至 2020-03-23"
flower_right = "专属花朵"
AI_right = "AI测评"
skin_right = "专属皮肤"
discount_right = "优惠入班"
download_right = "记录下载"
flower_right_text = "会员定制花朵 任性送老师"
AI_right_text = "孩子的专属智能 陪伴小助手"
skin_right_text = "会员标识及皮肤 彰显与众不同"
discount_right_text = "会员购买打卡课程 可享受专属折扣"
download_right_text = "学习打卡记录 随时下载"

my_notebook = "日记本"
my_coupon = "优惠券"
my_comment = "我的评论"
my_praise = "我的赞"
gift_exchange = "礼物兑换"
chart = "排行榜"
mine_share = "分享小熊打卡"
mine_help = "帮助与反馈"


class Mine(Home):

    def __init__(self, driver):
        self.mine = Home(driver)
        self.base = self.mine.base
        self.mine.mine_tab()

    def mine_comment(self):
        self.base.click(my_comment, my_comment)

    def mine_balance(self):
        self.base.click(balance, balance)

    def mine_diamont_pay(self):
        self.base.click(diamont_pay, diamont_pay)

    def mine_rights(self, right_element):
        self.base.wait_element_appear(account_num, account_num)
        self.base.click(right_element, right_element)

    def mine_priaise(self):
        self.base.click(my_praise, my_praise)

    def mine_notebook(self):
        self.base.wipe_up()
        self.base.click(my_notebook, my_notebook)

    def mine_coupon(self):
        self.base.wipe_up()
        self.base.click(my_coupon, my_coupon)

    def mine_gift(self):
        self.base.wipe_up()
        self.base.click(gift_exchange, gift_exchange)

    # TODO 礼物兑换需要补足用例

    def mine_chart(self):
        self.base.wipe_up(1)
        self.base.click(chart, chart)

    def mine_share(self):
        self.base.wipe_up()
        self.base.click(mine_share, mine_share)

    def mine_help(self):
        self.base.wipe_up()
        self.base.click(mine_help, mine_help)

