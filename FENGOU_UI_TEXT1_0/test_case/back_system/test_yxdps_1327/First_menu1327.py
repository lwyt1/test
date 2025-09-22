import time

from common import common_config


def Frist_menu1327(driver):
    username = "xuwenchao"
    password = "123456"
    common_config.ff(driver).login(username, password)
    time.sleep(1)
    common_config.ff(driver).jubing("window.open();")
    driver.get("http://admin.fengou206.com/Public/main")


