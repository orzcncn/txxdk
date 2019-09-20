#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-19 09:45
# @Author  : Innocence
# @Site    : 
# @File    : base.py
# @Software: PyCharm

import re, time
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


class Base(object):

    def __init__(self, driver):
        self.d = driver
        self.width = self.get_window_size()[0]
        self.height = self.get_window_size()[1]

    def click(self, element, log_text):
        """
        元素点击
        element:元素名称
        log_text:打印log的文案
        xpath使用方法
        1.包含
        d.xpath(u"//android.widget.TextView[contains(@text,'购买 ¥')]").click()
        2.全匹配
        d.xpath(u"//android.widget.TextView[@text='购买 ¥4.99']").click()
        3.匹配开始字符
        d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ¥')]").click()
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).click()
        elif re.findall("//", str(element)):
            self.d.xpath(element).click()
        else:
            self.d(text=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def click_advance(self, element_list):
        """
        根据绝对坐标点击 包含坐标和坐标描述
        例：{"location":(0.848, 0.91),"description":"修改"}
        :param element_list:
        :return:
        """
        x = element_list["location"][0]
        y = element_list["location"][1]
        self.d.click(x, y)
        logger.info("点击元素「{}」".format(element_list["description"]))

    def send_keys(self, element, sendtext, log_text):
        """
        文本输入
        element:元素名称
        sendtext:输入的文案
        log_text:打印log的文案
        :return:
        """
        if str(element).startswith("com"):
            self.d(resourceId=element).set_text(sendtext)
        elif re.findall("//", str(element)):
            self.d.xpath(element).set_text(sendtext)
        else:
            self.d(text=element).set_text(sendtext)

        logger.info("输入文字「{}」".format(log_text))

    def click_web(self, element, log_text):
        
        """
        通过文字,点击web页面中的元素
        element=u"文化艺术"
        :return:
        """

        self.d(description=element).click()
        logger.info("点击元素:「{}」".format(log_text))

    def double_click(self, x, y, time=0.5):
        """
        双击
        :return:
        """
        self.d.double_click(x, y, time)
        logger.info("点击坐标:「{}」,「{}」".format(x, y))

    def get_window_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[1])
        return width, height

    def wipe_up(self, duration=0.5):
        """
        向上滑动,查看下面的内容
        :return:
        """
        self.d.drag(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, duration)
        logger.info("向上滑动")

    def wipe_down(self, duration=0.5):
        """
        向下滑动，查看上面的内容
        :return:
        """
        self.d.drag(self.width / 2, self.height / 4, self.width / 2, self.height * 3 / 4, duration)
        logger.info("向下滑动")

    def direction_swipe(self, direction, element, steps=200):
        """
        方向滑动
        :param direction: 方向
        :param element:  元素
        :param steps:  1 steps is about 5ms, so 20 steps is about 0.1s
        :return:
        """
        self.d(text=element).swipe(direction, steps=steps)

    def swipe_to_element(self, element1, element2, duration=0.25):
        """
        滑动到某个元素
        :param element1: 起始元素
        :param element2: 目标元素
        :param duration: 滑动时间
        :return:
        """
        self.d(text=element1).drag_to(text=element2, duration=duration)
        logger.info("拖动元素「{}」至元素「{}」处".format(element1,element2))
        
    def wipe_down_element(self, element):
        """
        向下滑动到某个元素
        :return:
        """
        # is_find = False
        max_count = 5
        while max_count > 0:
            if self.find_elements(element):
                logger.info("向下滑动到:「{}」".format(element))
            else:
                self.wipe_down()
                max_count -= 1
                logger.info("向下滑动")

    def wipe_up_element(self, element):
        """
        向上滑动到某个元素
        :return:
        """
        # is_find = False
        max_count = 10
        while max_count > 0:
            if self.find_elements(element):
                logger.info("向上滑动到:「{}」".format(element))
            else:
                self.wipe_up()
                max_count -= 1
                logger.info("向上滑动")

    def back(self):
        """
        模拟物理键返回
        :return:
        """
        self.d.press("back")
        logger.info("点击返回")

    def toast_show(self, text, duration=5):
        """
        页面出现弹窗提示时间，默认时间5s
        :param text:弹窗内容
        :param duration:弹窗提示时间
        :return:
        """
        self.d.toast.show(text, duration)
        logger.info("展示文字")

    def wait_element_appear(self, element, log_text, timeout=5):
        """
        等待某个元素的出现，默认等待时间5s
        :param element: 元素内容
        :param log_text:log元素内容
        :param timeout:超时时间
        :return:
        """
        self.d(text=element).wait(timeout=timeout)
        logger.info("等待「{}」元素出现".format(log_text))

    def wait_element_gone(self, element, log_text, timeout=2):
        """
        等待某个元素的消失，默认等待时间5s
        :param element: 元素内容
        :param log_text:log元素内容
        :param timeout:超时时间
        :return:
        """
        self.d(text=element).wait_gone(timeout=timeout)
        logger.info("等待「{}」元素消失".format(log_text))

    def find_elements(self, element, timeout=5):
        """
        查找元素是否存在当前页面
        :param element: 元素内容
        :param timeout:log元素内容
        :return:
        """
        is_exist = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element, xml):
                    is_exist = True
                    logger.info("查询到「{}」".format(element))
                    break
                else:
                    timeout -= 1
        except Exception as e:
            logger.info("「{}」查找失败!「{}」".format(element, e))
        finally:
            return is_exist

    def elements_exist(self, element):
        """
        断言当前页面元素情况，用于判断多个页面状态的判断
        :param element:
        :return:
        """
        is_exist = False
        if self.d(text=element).exists(timeout=5):
            is_exist = True
        return is_exist

    def assert_exist(self, element):
        """
        断言当前页面存在要查找的元素,存在则判断成功
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        assert self.d(text=element).exists(timeout=5) == True, "断言「{}」元素存在,失败了!".format(element)
        logger.info("断言「{}」元素存在,成功了!".format(element))

    def assert_not_exist(self, element):
        """
        假设九秒走满 还没有找到这个页面有这个元素 判断这个页面元素不存在
        wait Settings appear in 3s, same as .wait(3)
        :param element:
        :return:
        """
        start_time = time.time()
        self.d(text=element).exists(timeout=10)
        end_time = time.time()
        assert (end_time-start_time > 9) == True ,"断言「{}」元素不存在,失败了!".format(element)
        logger.info("断言「{}」元素不存在,成功了!".format(element))


    def assert_contain_text(self, localtion, element):
        """
        断言页面的某个位置是否含有该文字
        :param localtion: 直接是x,y 坐标
        :param element:
        :return:
        """
        element_details = self.d(localtion).info
        assert element == element_details["text"], "断言「{}」位置没有「{}」元素失败!".format(localtion, element)
        logger.info("断言「{}」位置存在「{}」元素成功!".format(localtion, element))


    def wait_time(self, timeout=2):
        time.sleep(timeout)
