# author:丑牛
# 智能工作面信息平台页面自动化

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()  # 创建Chrome对象.

driver.get('http://login.cloud.zhengmeiji.com.cn:81/index.html')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/section/div/form/div[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/section/div/form/div[2]/ul/li[1]').click()
# user = input("用户名: ")
driver.find_element_by_xpath('/html/body/div/section/div/form/div[3]/input').send_keys(
    "wangzhaoxian")
# password = input("密码: ")
driver.find_element_by_xpath('/html/body/div/section/div/form/div[4]/input').send_keys("wzx670905")
driver.find_element_by_xpath('/html/body/div/section/div/form/div[5]/div[2]/button').click()
# driver.implicitly_wait(30)
dic6 = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]")
# company_name = input("请输入集团名称: ")
# if company_name == '枣矿集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[1]")
# elif company_name == '陕煤集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[2]")
# elif company_name == '平煤集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[3]")
# elif company_name == '沈煤集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[4]")
# elif company_name == '神火集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[5]")
# elif company_name == '徐矿集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[6]")
# elif company_name == '京能集团昊华精煤':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[7]")
# elif company_name == '晋能煤业':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[8]")
# elif company_name == '淮北矿业':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[9]")
# elif company_name == '皖北煤电':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[10]")
# elif company_name == '首钢福山':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[11]")
# elif company_name == '鲁泰集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[12]")
# elif company_name == '冀中能源':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[13]")
# elif company_name == '沈阳焦煤':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[14]")
# elif company_name == '新矿集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[15]")
# elif company_name == '河南能源':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[16]")
# elif company_name == '国家能源集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[17]")
# elif company_name == '裕隆集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[18]")
# elif company_name == '伊泰集团':
#     target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[19]")

target = driver.find_element_by_xpath("//section[@class='page-center']/div/div[1]/div[19]")
ActionChains(driver).click_and_hold(dic6).move_to_element_with_offset(to_element=target, xoffset=30,
                                                                      yoffset=10).click(
    target).perform()
ActionChains(driver).release()
target.click()
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/a[2]/div').click()
# time.sleep(1)
canvas_elem = driver.find_element_by_xpath('//*[@id="zmj_support_pressure_chart"]/div[1]/canvas')
# print(canvas_elem.rect, canvas_elem.id)
canvas_elem.click()
# ActionChains(driver).move_to_element_with_offset(to_element=target, xoffset=100, yoffset=20).perform()
# time.sleep(0.5)
# ActionChains(driver).move_to_element_with_offset(to_element=target, xoffset=200, yoffset=50).perform()
time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="zmj_charts_aera"]/div[1]/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/label[3]/div/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[6]').click()
driver.find_element_by_xpath(
    '//*[@id="zmj_charts_aera"]/div[1]/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/button/span').click()
driver.quit()