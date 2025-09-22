import time

from common import common_config


class First_menu:
    def menu(self,driver):

        username = "limengfei"
        password = "123456"
        common_config.ff(driver).login(username, password)
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")  #跳至指定页面
        driver.get("http://admin.fengou206.com/Super/SuperBkApply/index")
        common_config.ff(driver).xpath("//*[@name='item_id']").send_keys("746963180033")
        common_config.ff(driver).enter()
