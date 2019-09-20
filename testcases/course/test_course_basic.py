#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 15:21
# @Author  : Innocence
# @Site    : 
# @File    : test_course_basic.py
# @Software: PyCharm

import pytest, allure
from module.course.course_basic import Coursebasic
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


@pytest.mark.usefixtures("driver_setup")
@allure.feature("用户课程页面")
class Testcoursebasic:

    @pytest.fixture()
    def init_course(self):
        self.course = Coursebasic(self.driver)
        self.base = self.course.base
        logger.info("初始化基础课程页面")
        yield self.course
        logger.info("结束基础课程页面")

    @allure.story("进入送花列表")
    def test_course_flow_list(self, init_course):
        init_course.course_basic_flow_list()
        self.base.assert_exist("给老师送花")

    @allure.story("客服引导公众号关注")
    def test_course_customer_ad(self, init_course):
        init_course.course_basic_customer_ad()
        self.base.assert_exist("客服会话")

    @allure.story("进入基本设置")
    def test_course_settings(self, init_course):
        init_course.course_basic_settings()
        self.base.click("邀请打卡", "设置")
        self.base.click_advance({"location": (0.892, 0.296), "description": "切换点评消息提醒"})
        self.base.assert_exist("群主点评消息提醒")
        self.base.click("保存并退出 ", "保存并退出")
        self.base.assert_not_exist("群主点评消息提醒")

    @allure.story("进入打卡")
    def test_course_enter_punch(self, init_course):
        init_course.course_basic_punch()
        self.base.assert_exist("录音")
        self.base.assert_exist("图片")
        self.base.assert_exist("视频")
        self.base.send_keys("记录今天的感想和收获吧~", "测试打卡内容", "测试打卡内容")
        self.base.back()
        self.base.click("发表日志", "发表日志")
        self.base.assert_exist("删除")

    @allure.story("送花")
    def test_course_send_flow(self, init_course):
        init_course.course_basic_send_flow()
        self.base.click("送出", "送出")
        self.base.wait_element_gone("绘制送花图片中", "绘制送花图片中", 10)
        self.base.click("确认送出", "确认送出")
        self.base.click("com.tencent.mm:id/az_", "确认")
        self.base.assert_exist("送花")

    @allure.story("进入消息中心")
    def test_course_message(self, init_course):
        init_course.course_basic_message()
        self.base.click("点赞评论(0)", "点赞评论(0)")
        self.base.click("系统消息(0)", "系统消息(0)")
        self.base.assert_exist("暂无未读消息")

    @allure.story("进入排行榜")
    def test_course_charts(self, init_course):
        init_course.course_basic_charts()
        self.base.assert_exist("任天野")
        self.base.click("鲜花榜", "鲜花榜")
        self.base.assert_exist("我也去送花")
        self.base.click("勋章榜", "勋章榜")
        self.base.assert_exist("赶紧成为排行榜第一名")

    @allure.story("用户分享")
    def test_course_share_button(self, init_course):
        init_course.course_basic_share_button()
        self.base.assert_exist("创建新聊天")

    # @allure.story("筛选")                         # 管理员处回归
    # def test_course_filter(self, init_course):
    #     init_course.course_basic_filter()

    @allure.story("更多课程")
    def test_course_more_course(self, init_course):
        init_course.course_basic_more_course()
        self.base.assert_exist("家庭教育收费班级")

    @allure.story("快捷导航")
    def test_course_navigate(self, init_course):
        init_course.course_basic_navigate()
        self.base.click_advance({"location": (0.912, 0.742), "description": "导航去送花"})
        self.base.assert_exist("添加祝福语")

    @allure.story("发表评论")
    def test_course_comment(self, init_course):
        self.base.wait_time(1)
        init_course.course_basic_comment()
        self.base.wait_time(1)
        self.base.send_keys("写评论", "这是评论", "评论")
        self.base.back()
        self.base.wait_time(1)
        self.base.click("发表评论 ", "发表评论")
        self.base.assert_exist("Rhapsody")

    @allure.story("删除评论")
    def test_delete_course_comment(self, init_course):
        self.base.click("Rhapsody", "Rhapsody")
        self.base.click_advance({"location": (0.506, 0.901), "description": "删除评论"})
        self.base.click("com.tencent.mm:id/az_", "确认删除")

    @allure.story("点赞")
    def test_course_praise(self,init_course):
        self.base.wait_time(1)
        init_course.course_basic_praise()
        self.base.assert_exist("点赞成功 +1分")

    @allure.story("日记分享")
    def test_course_diary_share(self, init_course):
        init_course.course_basic_diary_share()
        self.base.assert_exist("创建新聊天")

    @allure.story("查看今日打卡内容")
    def test_course_basic_diary_view(self, init_course):
        init_course.course_basic_diary_view()
        self.base.assert_exist("日记本")
