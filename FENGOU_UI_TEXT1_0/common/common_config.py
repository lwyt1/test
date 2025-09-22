import time

import ddddocr
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CommonFunction:
    def __init__(self,driver):
        self.driver = driver

    # 登录
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@name="account"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@name="password"]').send_keys(password)
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[@name="verify"]').clear()
            except Exception as e:
                break
            # 截取验证码
            self.driver.find_element(By.XPATH, '//*[@id="verifyImg"]').screenshot("code.png")
            # 输入验证码
            ocr = ddddocr.DdddOcr(show_ad=False)  # 创建一个ocr识别对象
            with open('code.png', 'rb') as f:
                img_bytes = f.read()  # 把验证码图片在python中读取成字节流
            res = ocr.classification(img_bytes)  # 识别验证码
            # 获取的验证码写入文本框
            self.driver.find_element(By.XPATH, '//*[@name="verify"]').send_keys(res)
            # 点击登录
            self.driver.find_element(By.XPATH, '//*[@id="checkList"]/tbody/tr[10]/td/input[2]').click()
            time.sleep(2)##

    def id(self, id):  # 通过id定位
        return self.driver.find_element(By.ID, id)

    def cls_name(self, cls):  # 通过class_name定位
        return self.driver.find_element(By.CLASS_NAME, cls)

    def name(self, n):  # 通过name定位
        return self.driver.find_element(By.NAME, n)

    def tag_name(self, a):
        return self.driver.find_element(By.TAG_NAME, a).click()

    def xpath(self, x):  # 通过xpath定位
        return self.driver.find_element(By.XPATH, x)

    def eles(self, x ):  # 定位多个位置
        return self.driver.find_elements(By.XPATH, x)

    def to_text(self, x):  # 输出文本
        return self.xpath(x).text

    def getas(self, x, g):  # 定位值获取标签元素
        return self.xpath(x).get_attribute(g)

    def getas_cls(self,x,g): #通过class_name 定位 标签元素
        return self.cls_name(x).get_attribute(g)

    def send(self, x, s):  # 输入值
        self.xpath(x).send_keys(s)

    def send_name(self, x, s):  # 输入值
        self.cls_name(x).send_keys(s)

    def click(self,x): #输入值单击
        self.xpath(x).click()

    def jubing(self, x):
        self.driver.execute_script(x)  # 打开一个新的浏览器窗口 x="window.open();"
        handles = self.driver.window_handles  # 获取当前所有窗口的句柄
        self.driver.switch_to.window(handles[-1])  # 切换到最后一个窗口

    def switch(self, a):  # 切入框架
        return self.driver.switch_to.frame(a)

    def switch_to(self):  # 切出框架
        return self.driver.switch_to.default_content()  # 跳出框架



    def context(self, x):  # 右键操作
        ActionChains(self.driver).context_click(x).perform()

    def double(self, x):  # 双击
        ActionChains(self.driver).double_click(x).perform()

    def move(self, x):  # 悬浮
        ActionChains(self.driver).move_to_element(x).perform()

    # def click(self, x):  # 点击
    #     ActionChains(self.driver).click_and_hold(x).perform()

    def action_send(self, x):  # 模拟键盘输入
        ActionChains(self.driver).send_keys(x).perform()

    def enter(self):  # 模拟键盘回车
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def ctrl(self, x):  # 模拟键盘Ctrl组合键
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(x).perform()

    def tab(self):  # tab键
        ActionChains(self.driver).send_keys(Keys.TAB).perform()


ff = CommonFunction
