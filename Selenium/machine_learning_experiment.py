# author:丑牛
# 机器学习平台

from selenium import webdriver
import time


driver = webdriver.Chrome()  # 创建Chrome对象.

driver.get('http://192.168.94.128:3000/machine-learn-system/index.html')
driver.implicitly_wait(60)
driver.maximize_window()
# title = driver.title
# print(title)
# driver.find_element_by_xpath('//a[@href="#/experiment"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//span[contains(text(),"新增实验")]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//span[contains(text(),"取 消")]').click()
# time.sleep(1)
# # 新增
# driver.find_element_by_xpath('//span[contains(text(),"新增实验")]').click()
# time.sleep(1)
# text = driver.find_element_by_xpath('//span[@class="el-dialog__title"]').text
# print(text)
# time.sleep(1)
# driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').clear()
# driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
# text = driver.find_element_by_class_name('error-tips').text
# print(text)
# driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').send_keys("test")
# driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').clear()
# driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').send_keys("testshiyan")
# time.sleep(1)
# driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
# time.sleep(1)
# 修改
driver.find_element_by_xpath('//li[contains(text(),"3")]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[contains(text(),"Ctest")]').click()
jude1 = driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').is_enabled()
print(jude1)
jude2 = driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').is_enabled()
print(jude2)
driver.find_element_by_xpath('//span[contains(text(),"编 辑")]').click()
time.sleep(1)
jude1 = driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').is_enabled()
print(jude1)
jude2 = driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').is_enabled()
print(jude2)
driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').clear()
text = driver.find_element_by_class_name('error-tips').text
print(text)
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="请输入实验名称"]').send_keys("test1")
driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').clear()
driver.find_element_by_xpath('//textarea[@placeholder="请输入模型描述"]').send_keys("tests")
time.sleep(1)
driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
time.sleep(1)
# # 打开
# driver.refresh()
# driver.find_element_by_xpath('//li[contains(text(),"2")]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//div[contains(text(),"test1")]/../../following-sibling::div[1]/button/span[contains(text(),"打开")]').click()
# # driver.find_element_by_xpath('//div[contains(text(),"test1")]/../../following-sibling::div[1]/button/span[contains(text(),"打开")]').click()
# driver.find_element_by_xpath('//span[contains(text(),"编排")]/span').click()
# time.sleep(1)
# # 删除-取消
# driver.find_element_by_xpath('//li[contains(text(),"2")]').click()
# driver.find_element_by_xpath('//div[contains(text(),"test1")]/../../following-sibling::div[1]/button/span[contains(text(),"删除")]').click()
# # driver.find_element_by_xpath('//div[contains(text(),"test1")]/../../following-sibling::div[1]/button/span[contains(text(),"删除")]').click()
# driver.find_element_by_xpath('//span[contains(text(),"取消")]').click()
# # 删除-确定
# time.sleep(1)
# driver.find_element_by_xpath('//li[contains(text(),"2")]').click()
# driver.find_element_by_xpath(
#     '//div[contains(text(),"test1")]/../../following-sibling::div[1]/button/span[contains(text(),"删除")]').click()
# text = driver.find_element_by_xpath('//div[@class="el-message-box__message"]').text
# print(text)
# driver.find_element_by_xpath('//span[contains(text(),"确定")]').click()
# time.sleep(2)
# a = driver.find_elements_by_class_name('right-cont-title')
# # a = driver.find_elements('By.xpath', '//div[@class="right-cont-title")')
# for i in a:
#     print(i.text)
driver.quit()
