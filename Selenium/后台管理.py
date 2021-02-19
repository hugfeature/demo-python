# author:丑牛
# 矿级后台管理工作面

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()  # 创建Chrome对象.

driver.get('http://codeui.cloud.zhengmeiji.com.cn:81/#/login')
driver.implicitly_wait(60)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[1]/div/div/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[1]/div/div/input').send_keys('wangzhaoxian')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/input').send_keys('wzx670905')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/form/div[3]/div/button').click()
