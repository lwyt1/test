import time

import allure

from common import common_config

class Testloginadmin:
    def test001(self ,init_driver):
        driver = init_driver
        common_config.ff(driver).login('admin','123456');
        pass

