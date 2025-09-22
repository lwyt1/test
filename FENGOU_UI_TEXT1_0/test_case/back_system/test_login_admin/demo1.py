import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()
# driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("吴亦凡")
# driver.find_element(By.ID,'su').click()
time.sleep(2)

# driver.find_element(By.CLASS,'mnav c-font-normal c-color-t').click()
driver.find_element(By.XPATH,'//*[text()="新闻"] ')
# print(a)
pass
# # XPath提取文本
# texts = driver.find_elements(By.XPATH, "//div//text()")
# # CSS选择器提取文本
# text = driver.find_element(By.CSS_SELECTOR, ".class").text