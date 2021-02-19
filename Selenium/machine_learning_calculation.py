# author:丑牛
# 机器学习平台

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from icecream import ic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # 创建Chrome对象.
try:
    driver.get('http://192.168.94.128:3000/machine-learn-system/index.html')
    driver.implicitly_wait(60)
    driver.maximize_window()
    # 打开算法页面
    driver.find_element_by_xpath('//a[@href="#/calculation/index"]').click()
    time.sleep(1)
    text = driver.find_element_by_class_name('page-title-name').text
    ic(text)
    # # 新建算法
    # driver.find_element_by_xpath('//span[contains(text(),"新 建")]').click()
    # time.sleep(1)
    # text = driver.find_element_by_class_name('el-dialog__title').text
    # print(text)
    # # 表单校验
    # driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
    # time.sleep(1)
    # elements = driver.find_elements_by_class_name('error-tips')
    # textlist = []
    # ic(elements)
    # for i in elements:
    #     ic(type(i))
    #     ic(i.text)
    #     textlist.append(i.text)
    # # 取消校验
    # driver.find_element_by_xpath('//span[contains(text(),"取 消")]').click()
    # # 新建算法
    # driver.find_element_by_xpath('//span[contains(text(),"新 建")]').click()
    # time.sleep(1)
    # driver.find_element_by_name('identifier').send_keys('test1')
    # driver.find_element_by_name('name').send_keys('test1')
    # driver.find_element_by_xpath('//input[@placeholder="请选择算法框架"]').click()
    # driver.find_element_by_xpath('//span[contains(text(),"spark")]').click()
    # time.sleep(1)
    # # 元素分类
    # driver.find_element_by_xpath('//body/div[@id="app"]/div[1]/div[2]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/form[1]/div[4]/div[1]/span[1]/div[1]/div[1]/span[1]/span[1]/i[1]').click()
    # time.sleep(2)
    # divs = driver.find_elements_by_xpath('//span[contains(text(),\'机器学习算法\')]')
    # ic(len(divs))
    # divs[1].click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'模型导出\')]').click()
    # time.sleep(1)
    # # 上传文件
    # driver.find_element_by_name('file').send_keys('C:\\Users\\wangzhaoxian\\Downloads\\1.csv')
    # time.sleep(2)
    # # 上传文件-文件覆盖
    # driver.find_element_by_name('file').send_keys('C:\\Users\\wangzhaoxian\\Downloads\\2.parquet')
    # time.sleep(2)
    # driver.find_element_by_xpath('//input[@placeholder="请输入算法主类"]').send_keys('test1')
    # time.sleep(1)
    # driver.find_element_by_xpath('//textarea[@placeholder="请输入规格参数"]').send_keys('[]')
    # time.sleep(1)
    # driver.find_element_by_xpath('//textarea[@placeholder="请输入算法描述"]').send_keys('test1')
    # # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
    # time.sleep(1)
    # # 查询-重置
    # driver.find_element_by_xpath('//input[@placeholder="请输入算法名称"]').send_keys('test1')
    # driver.find_element_by_xpath('//span[contains(text(),"重 置")]').click()
    # time.sleep(1)
    # 查询-查询
    # driver.find_element_by_xpath('//input[@placeholder="请输入算法名称"]').send_keys('test1')
    # driver.find_element_by_xpath('//body/div[@id=\'app\']/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]').click()
    # driver.find_element_by_xpath('//span[contains(text(),\'机器学习算法\')]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'模型导出\')]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'查 询\')]').click()
    # time.sleep(1)
    # time1 = time.time()
    # # ele = driver.find_elements_by_xpath('//tbody/tr')
    # ele = driver.find_elements(By.XPATH, '//tbody/tr')
    # ic(len(ele))
    # time2 = time.time()
    # ic(time2 - time1)
    # if len(ele) == 0:
    #     text = driver.find_element_by_xpath("//span[contains(text(),'暂无数据')]").text
    #     ic(text)
    # # 修改
    # driver.find_element_by_xpath('//span[contains(text(),"重 置")]').click()
    driver.find_element_by_xpath('//input[@placeholder="请输入算法名称"]').send_keys('zmjtest')
    # # driver.find_element_by_xpath('//body/div[@id="app"]/div[1]/div[2]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/form[1]/div[4]/div[1]/span[1]/div[1]/div[1]/span[1]/span[1]/i[1]').click()
    # driver.find_element_by_xpath('//body/div[@id=\'app\']/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1]').click()
    # driver.find_element_by_xpath('//span[contains(text(),\'通用算法\')]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'特征工程\')]').click()
    # time.sleep(1)
    driver.find_element_by_xpath('//span[contains(text(),\'查 询\')]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//span[contains(text(),\'编辑\')]').click()
    time.sleep(1)
    text = driver.find_element_by_name('identifier').text
    ic(text)
    driver.find_element_by_xpath("//span[contains(text(),'取 消')]").click()
    time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'编辑\')]').click()
    # time.sleep(1)
    # driver.find_element_by_name('identifier').clear()
    # driver.find_element_by_name('identifier').send_keys('test1234')
    # driver.find_element_by_xpath("//span[contains(text(),'确 定')]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[contains(text(),\'查 询\')]').click()
    # time.sleep(1)
    # # 删除
    # driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
    # time.sleep(1)
    # driver.find_element_by_xpath("//span[contains(text(),'取消')]").click()
    # time.sleep(1)
    # # driver.find_element_by_xpath('//span[contains(text(),\'查 询\')]').click()
    # # time.sleep(1)
    # driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
    # time.sleep(1)
    # text = driver.find_element_by_class_name('el-message-box__message').text
    # ic(text)
    # driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
except NoSuchElementException as e:
    print(e)
    print(e.msg)
finally:
    driver.quit()
