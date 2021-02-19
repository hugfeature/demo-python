# author:丑牛
# 机器学习平台

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()  # 创建Chrome对象.
try:
    driver.get('http://localhost:3000/machine-learn-system/index.html')
    driver.implicitly_wait(60)
    driver.maximize_window()
    driver.find_element_by_xpath('//a[@href="#/data/index"]').click()
    time.sleep(1)
    text = driver.find_element_by_class_name('page-title-name').text
    print(text)
    # # 重置
    # driver.find_element_by_xpath('//input[@placeholder="请输入数据名称"]').send_keys('测试数据111')
    # driver.find_element_by_xpath('//input[@placeholder="请选择"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),"csv")]')
    # driver.find_element_by_xpath("//span[contains(text(),'重 置')]").click()
    # text = driver.find_element_by_xpath('//input[@placeholder="请输入数据名称"]').text
    # print(text)
    # # 查询
    # driver.find_element_by_xpath('//input[@placeholder="请输入数据名称"]').send_keys('test')
    # driver.find_element_by_xpath('//input[@placeholder="请选择"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),"csv")]')
    # driver.find_element_by_xpath("//span[contains(text(),'查 询')]").click()
    # time.sleep(1)
    # ele = driver.find_element_by_xpath('//tbody').find_elements_by_tag_name('tr')
    # print(len(ele))
    # if len(ele) == 0:
    #     text = driver.find_element_by_xpath("//span[contains(text(),'暂无数据')]").text
    #     print(text)
    # 新建-DB
    # driver.find_element_by_xpath("//span[contains(text(),'新 建')]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//span[contains(text(),'确 定')]").click()
    # eles = driver.find_elements_by_class_name('error-tips')
    # for ele in eles:
    #     print(ele.text)
    # driver.find_element_by_xpath("//span[contains(text(),'取 消')]").click()
    driver.find_element_by_xpath("//span[contains(text(),'新 建')]").click()
    time.sleep(5)
    # driver.find_element_by_xpath("//div[@class='el-radio-group']/label[1]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@class='el-radio-group']/label[2]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@class='el-radio-group']/label[3]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//div[@class='el-radio-group']/label[1]").click()
    # time.sleep(1)
    driver.find_element_by_xpath('//input[@name="name"]').send_keys('test-db')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="jdbc://..."]').send_keys('test-db')
    driver.find_element_by_xpath('//input[@placeholder="请选择数据类型"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//span[contains(text(),"mysql")]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//textarea[@placeholder="请输入SQL命令"]').send_keys('test-db')
    driver.find_element_by_xpath("//span[contains(text(),'确 定')]").click()
except NoSuchElementException as e:
    print(e.msg)
finally:
    driver.quit()