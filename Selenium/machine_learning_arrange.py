# author:丑牛
# 机器学习平台

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()  # 创建Chrome对象.

driver.get('http://localhost:3000/machine-learn-system/index.html')
driver.implicitly_wait(60)
driver.maximize_window()
driver.find_element_by_xpath('//a[@href="#/arrange/index/:expId"]').click()

a = driver.find_elements_by_class_name('right-cont-title')
for i in a:
    print(i.text)
driver.quit()
