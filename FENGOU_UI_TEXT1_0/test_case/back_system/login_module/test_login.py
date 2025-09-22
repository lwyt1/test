import allure

from common import common_config


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("登录模块")
class TestLogin:
    @allure.story('登录模块 -- 登录功能')
    @allure.title('case_01 -- 验证正确的用户名和密码能否成功登录')
    def test_case_01(self, init_driver):
        driver = init_driver
        common_config.CommonFunction(driver).login("admin","123456")
        actual_result = driver.current_url
        assert actual_result == "http://admin.fengou206.com/"