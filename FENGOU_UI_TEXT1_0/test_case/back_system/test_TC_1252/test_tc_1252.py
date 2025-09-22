import time

import allure

from common import common_config


@allure.epic("crm后台——UI自动化测试项目")
@allure.feature("弹窗调整提醒模块")
#@pytest.mark.run_case
#@pytest.mark.skip(reason="跳过该模块")
########################################## 执行该模块时确保yanjiahui，xiongjingjing,wangjiankang账号正常弹窗 ###########################################
class TestTC1252:
    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_001 -- 登录后点击否 是否可以提交')
    @allure.description("登录后，弹窗直接点击否，然后点击提交")
    def test_case_001(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("yanjiahui", "123456")
        common_config.ff(driver).switch('main')
        common_config.ff(driver).xpath( "//input[@value='-1']").click()  # 点击否
        common_config.ff(driver).xpath("//*[text()='提交']").click()
        actual_result = common_config.ff(driver).xpath("//*[text()='月小组业绩排行']").text
        assert actual_result == "月小组业绩排行"

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_002 -- 登录后是否出现弹窗')
    def test_case_002(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        common_config.ff(driver).switch("main")  # 切入
        actual_result = common_config.ff(driver).to_text("//*[text()='用户机使用情况反馈']")# 打印实际结果
        expected_result = '用户机使用情况反馈'  # 预期
        assert expected_result == actual_result

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_003 -- 弹窗直接提交是否出现提示')
    def test_case_003(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        common_config.ff(driver).switch("main")  # 切入
        common_config.ff(driver).tag_name('button')
        actual_result = common_config.ff(driver).to_text('//*[@class="layui-layer-move"]')#打印实际结果
        expected_result = "请填写反馈内容！"
        assert actual_result != expected_result

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_004 -- 弹窗点击是 是否可以继续操作')
    def test_case_004(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        common_config.ff(driver).switch("main")  # 切入
        common_config.ff(driver).xpath("//input[@value='1']").click() # 点击是
        actual_result = common_config.ff(driver).to_text("//*[contains(text(),'机号是否可以正常拨打')]")
        assert actual_result.__contains__('2、你的工作手机&手机号是否可以正常拨打电话')

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_005 -- 弹窗工作机使用点击否 是否提示输入原因')
    def test_case_005(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        driver.switch_to.frame("main")
        common_config.ff(driver).click("//input[@value='1']") # 第一个是
        common_config.ff(driver).click("//input[@name='boda'and @value='-1']")# 第二个否
        actual_result = common_config.ff(driver).getas_cls('form-control',"placeholder")
        assert actual_result == "请输入不能正常使用的原因。"

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_006 -- 弹窗工作机使用点击否 输入框输入显示是否一致')
    def test_case_006(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        driver.switch_to.frame("main")
        common_config.ff(driver).click("//input[@value='1']")# 第一个是
        common_config.ff(driver).click("//input[@name='boda'and @value='-1']")# 第二个否
        value1 = common_config.ff(driver).cls_name('form-control')
        value1.send_keys("工作机损坏\n")
        actual_result = value1.get_attribute('value')
        assert actual_result == "工作机损坏"

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_007 -- 弹窗工作机更换选择是否可以切换')
    def test_case_007(self, init_driver):
        global value1
        dist = []
        driver = init_driver
        common_config.ff(driver).login("xiongjingjing", "123456")
        driver.switch_to.frame("main")
        common_config.ff(driver).click("//input[@value='1']")# 第一个是
        common_config.ff(driver).click("//input[@name='boda'and @value='-1']")# 第二个否
        el = common_config.ff(driver).eles("//*[@name='kadun']")
        #el = driver.find_elements(By.XPATH, "//*[@name='kadun']")
        for els in el:
            els.click()
            value1 = els.get_attribute('value')
            time.sleep(1)
            dist.append(value1)
        print(dist)
        assert dist.__contains__(value1)

    @allure.story('弹窗调整提醒模块 -- 弹窗提醒功能')
    @allure.title('case_008 -- 弹窗工作机更换选择后提交是否有效')
    def test_case_008(self, init_driver):
        driver = init_driver
        common_config.ff(driver).login("wangjiankang", "123456")
        driver.switch_to.frame("main")
        common_config.ff(driver).click("//input[@value='1']")  # 第一个是
        common_config.ff(driver).click("//input[@name='boda'and @value='-1']")  # 第二个否
        common_config.ff(driver).send_name('form-control',"工作机损坏\n")
        common_config.ff(driver).click("//input[@name='kadun'and @value='0']")
        common_config.ff(driver).click("//*[text()='提交']")
        actual_result = common_config.ff(driver).to_text( "//*[text()='月小组业绩排行']")
        assert actual_result == "月小组业绩排行"