import time

from common import common_config

class Frist_menu1327:
    def Frist_menu1327(self,driver):
        username = "xuwenchao"
        password = "123456"
        common_config.ff(driver).login(username, password)
        time.sleep(1)
        common_config.ff(driver).jubing("window.open();")
        driver.get("http://admin.fengou206.com/Public/main")