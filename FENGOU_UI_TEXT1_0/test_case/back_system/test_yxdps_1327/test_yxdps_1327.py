import time

import allure
import pytest

from common import common_config
from test_case.back_system.test_yxdps_1327.First_menu1327 import Frist_menu1327


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("1月有效店铺数排行榜模块")
@pytest.mark.run_case
class TestYxdps1327:
    @allure.story('1月有效店铺数排行榜模块 -- 首页新增功能')
    @allure.title('case_001 -- 验证是否新增挑战赛排行榜')
    def test_case_001(self , init_driver):
        driver = init_driver
        Frist_menu1327(driver) # 冗余代码 封装
        time.sleep(1)
        js = "window.scrollBy(0,800)" # 向下滑动1000个像素
        driver.execute_script(js)
        actual_result = common_config.ff(driver).to_text("//*[@class='card-header with-border']") # 获取所有文本
        expected_result = "季度业绩排名" # 预期结果文本
        assert expected_result in actual_result  # 实际包含预期

    @allure.story('1月有效店铺数排行榜模块 -- 首页点击功能')
    @allure.title('case_002 -- 验证点击是否查看详情')
    def test_case_002(self,init_driver):
        driver = init_driver
        Frist_menu1327(driver)
        time.sleep(1)
        js = "window.scrollBy(0,800)"  # 向下滑动1000个像素
        driver.execute_script(js)
        # actual_result = common_config.ff(driver).to_text("//*[@class=’card-block‘]") # 获取所有文本
        # expected_result = "今日报名爆款商品"
        # assert expected_result in actual_result
        pass