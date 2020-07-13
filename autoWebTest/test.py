from selenium import webdriver
import time

# driver = webdriver.Chrome()
# url = 'http://10.68.62.22/login'
# driver.get(url)
# list = driver.find_elements_by_tag_name('input')
# for i in range(len(list)):
#     list[i].send_keys('admin')
# time.sleep(2)
# driver.find_element_by_class_name('el-button--medium').click()
# time.sleep(5)
# driver.find_element_by_class_name('iconkucun').click()
# list = driver.find_elements_by_class_name('text-wrap')
# list[2].click()


driver = webdriver.Chrome()
url = 'http://lms-rent-test.gtland.cn/?ticket=ST-2045-IO1TpdgFRiFT3UEtKojEloSxLQ0-test_app02#/home'
driver.get(url)
driver.find_element_by_id('username').send_keys('chenjianqi')
driver.find_element_by_id('password').send_keys('123456Abc')
driver.find_element_by_name('submit').click()
time.sleep(5)

driver.find_element_by_css_selector('.nav>li:nth-of-type(5)').click()