#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-02-26 14:53
# @Author  : Innocence
# @Site    : 
# @File    : run.py
# @Software: PyCharm

import pytest, os, subprocess
from tools.loggers import JFMlogging
logger = JFMlogging().getloger()


def init_env():
    cmd = "python3 -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python3 -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")


def init_report():
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


# init_env()
pytest.main(["-s", "-n 2", "--reruns=2", "testcases", "--alluredir=data"])
init_report()
