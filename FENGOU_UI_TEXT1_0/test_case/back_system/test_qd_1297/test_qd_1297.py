import time
import allure
import pytest
from test_case.back_system.test_qd_1297.Public_section import First_menu
from common import common_config


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("渠道一键2+1模块")
# @pytest.mark.run_case
class TestQd1297:
    @allure.story('渠道一键2+1模块 -- 【一键2+1】功能是否有效')
    @allure.title('case_001 -- 验证点击【一键2+1】弹窗是否弹出')
    def test_case_001(self, init_driver):
        driver = init_driver
        First_menu.menu(self,init_driver)
        common_config.ff(driver).xpath('//*[contains(text(),"一键2+1")]').click()
        time.sleep(1)
        actual_result = common_config.ff(driver).to_text('//*[@class="layui-layer-title"]')
        assert actual_result == "一键2+1重新报名"

    @allure.story('渠道一键2+1模块 -- 【一键2+1】功能是否有效')
    @allure.title('case_002 -- 验证点击【一键2+1】店铺显示是否一致')
    def test_case_002(self,init_driver):
        driver = init_driver
        First_menu.menu(self,init_driver)
        time.sleep(1)
        expected_result = common_config.ff(driver).to_text('//*[contains(text(),"佰瑞衡旗舰店")]')# 预期店铺名
        common_config.ff(driver).xpath('//*[contains(text(),"一键2+1")]').click()
        common_config.ff(driver).switch("layui-layer-iframe100001")#框架
        actual_result = common_config.ff(driver).to_text('//*[@id="J-formQuickTags2Plus1-600037"]')#实际 一键2+1所有文本
        assert expected_result in actual_result# 实际包含预期