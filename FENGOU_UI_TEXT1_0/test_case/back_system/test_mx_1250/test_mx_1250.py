import time

import allure
from selenium.webdriver.support.color import Color

from common import common_config


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("商家资源推广明细模块")
#@pytest.mark.run_case
#@pytest.mark.skip(reason="跳过该模块")
class TestMx1250:
    @allure.story('商家资源推广明细 -- 默认显示功能')
    @allure.title('case_001 -- 验证打开默认是否选择未处理')
    @allure.description('打开资源推广明细页，查看默认筛选状态')
    def test_case_001(self,init_driver):
        driver=init_driver
        common_config.ff(driver).login("yanzhijiang","123456")
        #  common_config.CommonFunction(driver).login("yanzhijiang","123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/CmsLiuliangbao/index")
        actual_result = common_config.ff(driver).getas("//input[@name='status'and @value='0']","value")
        assert actual_result=="0"

    @allure.story('商家资源推广明细 -- 默认显示功能')
    @allure.title('case_002 -- 验证商家推广资源明细提示词是否为红色（#a94442）')
    @allure.description("打开资源推广明细页，查看下方提示词是否为红色")
    def test_case_002(self, init_driver):
        driver = init_driver
        init_driver.username1="yanzhijiang"
        init_driver.password1="123456"
        common_config.ff(driver).login(init_driver.username1, init_driver.password1)
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/CmsLiuliangbao/index")
        aa = common_config.ff(driver).cls_name('text-danger')
        # print(aa.value_of_css_property('color')) # 获取color元素的CSS属性值
        # 查看rgba(169, 68, 66, 1)的hex格式
        actual_result = Color.from_string('rgba(169, 68, 66, 1)').hex
        expected_result = "#a94442"  # 预期
        assert actual_result == expected_result

    @allure.story('商家资源推广明细 -- 支持操作模块')
    @allure.title('case_003 -- 验证支持点击【查看dtk】是否跳转对应商品详情')
    @allure.description("登录支持——打开资源推广明细页——点击【查看dtk】按键")
    # @pytest.mark.skip(reason="跳过该模块")
    def test_case_003(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("chenjiaxin", "123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")
        #  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/CmsLiuliangbao/index")
        common_config.ff(driver).xpath('//*[text()="查看dtk"]').click()
        # driver.find_element(By.XPATH, '//*[text()="查看dtk"]').click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        actual_result = driver.current_url #获取当前跳转后的路径
        assert actual_result.__contains__("https://www.dataoke.com/xp/search?keywords")

    @allure.story('商家资源推广明细 -- 支持操作模块')
    @allure.title('case_004 -- 验证支持点击【选这个】是否出现原生弹窗')
    @allure.description("登录支持——打开资源推广明细页——点击【选这个】按键")
    def test_case_004(self, init_driver):
        driver = init_driver
        common_config.CommonFunction(driver).login("chenjiaxin", "123456")
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")# 打开一个新的浏览器窗口# 切换到最后一个窗口#  在当前窗口打开指定网址
        driver.get("http://admin.fengou206.com/Super/CmsLiuliangbao/index")
        common_config.ff(driver).xpath("//*[text()='选这个']").click()
        time.sleep(2)
        acc = driver.switch_to.alert  # 切入原生弹窗
        actual_result = acc.text  # 获取弹窗文字
        acc.dismiss()  # 取消操作
        assert actual_result == "确认要选这个商品吗？"