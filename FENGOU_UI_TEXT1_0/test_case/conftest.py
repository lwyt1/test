#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import pytest
from selenium import webdriver
from common import common_config
"""
-------------------------------------------------
   File Name：    
   Description : 产生driver
   Author :   xiaobei
   CreateDate：   
   wechat：xiaobei_upup
-------------------------------------------------
conftest.py测试框架pytest的胶水文件，里面用到了fixture的方法，封装并传递出了driver。
test_pytest.fixture 这个实现了和unittest的setup，teardown一样的前置启动，后置清理的装饰器。

管理数据库连接，全局管理我们的driver
"""
# 前置
@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://admin.fengou206.com/")
    driver.implicitly_wait(2)
# 后置
    yield driver
    driver.quit()

    # def close_brower():
    #     driver.quit()
    #
    # request.addfinalizer(close_brower)
    #
    # return driver














# @test_pytest.fixture(scope='session', autouse=True)
# def drivers(request):
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#
#     def fn():
#         driver.quit()
#
#     request.addfinalizer(fn)
#     return driver




#
# @test_pytest.fixture(scope='session', autouse=True)
# def drivers():
#     global driver
#     option = Options()
#     # 无头模式
#     option.add_argument('--headless')
#     # 沙盒模式运行
#     option.add_argument('--no-sandbox')
#     # 大量渲染时候写入/tmp而非/dev/shm
#     option.add_argument('disable-dev-shm-usage')
#     # 指定驱动路径
#     driver = webdriver.Chrome(chrome_options=option)
#
#     yield driver
#     driver.quit()














# @test_pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('用例名称'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.pop(2)
#
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)
#
#
# def pytest_html_results_table_html(report, data):
#     if report.passed:
#         del data[:]
#         data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))
#
#
# def _capture_screenshot():
#     '''
#     截图保存为base64
#     :return:
#     '''
#     return driver.get_screenshot_as_base64()
