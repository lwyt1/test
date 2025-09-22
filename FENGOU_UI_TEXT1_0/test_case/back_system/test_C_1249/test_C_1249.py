import time

import allure

from common import common_config


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("C店白名单模块")
# @pytest.mark.run_case
# @pytest.mark.skip(reason="跳过该模块")
class TestC1249:
    @allure.story('C店白名单模块 -- 店铺查询功能')
    @allure.title('case_001 -- 验证输入正确的待审核店铺是否可以查看')
    def test_case_001(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("limengfei", "123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")  # 打开一个新的浏览器窗口# 切换到最后一个窗口#  在当前窗口打开指定网址
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/SuperCrmShopWList/index")
        common_config.ff(driver).xpath('//*[@name="shop_name"]').send_keys("周黑鸭官方旗舰店")  # 定位查询框
        common_config.ff(driver).xpath('//*[@class="layui-btn"]').click()  # 点击查询
        actual_result = common_config.ff(driver).xpath('//*[@class="shop_name"]').text  # 打印实际结果
        print(actual_result)
        assert actual_result.__contains__("周黑鸭官方旗舰店")  # __contains__表示包含于
        assert actual_result == "周黑鸭官方旗舰店"

    @allure.story('C店白名单模块 -- 店铺查询功能')
    @allure.title('case_002 -- 验证输入错误的待审核店铺是否可以查看')
    def test_case_002(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("limengfei", "123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open(-1);")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/SuperCrmShopWList/index")

        common_config.ff(driver).xpath('//*[@name="shop_name"]').send_keys("xxxxx")
        common_config.ff(driver).xpath('//*[@class="layui-btn"]').click()
        # 预期结果
        expected_results = 'http://admin.fengou206.com/Super/SuperCrmShopWList/index'
        actual_result = driver.current_url
        assert actual_result != expected_results

    @allure.story('C店白名单模块 -- 招商查询功能')
    @allure.title('case_003 -- 验证输入正确招商名是否可以查看')
    def test_case_003(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("limengfei", "123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/SuperCrmShopWList/index")
        common_config.ff(driver).xpath('//*[@name="partner"]').send_keys("徐文超")
        common_config.ff(driver).xpath('//*[@class="layui-btn"]').click()
        actual_result = common_config.ff(driver).xpath('//*[@class="layui-table"]').text
        assert actual_result.__contains__("徐文超")

    @allure.story('C店白名单模块 -- 首页默认显示待审批')
    @allure.title('case_004 -- 验证进入页面默认待审批显示')
    def test_case_004(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("limengfei", '123456')
        common_config.ff(driver).jubing("window.open();")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/SuperCrmShopWList/index")
        driver.refresh()
        time.sleep(1)
        # 实际
        actual_result = common_config.ff(driver).getas('//*[text()="待审批"]', "text")
        assert actual_result.__contains__("待审批")
        # assert actual_result == "待审批"
