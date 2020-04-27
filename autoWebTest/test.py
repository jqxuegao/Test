from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'http://10.68.62.22/login'
driver.get(url)
list = driver.find_elements_by_tag_name('input')
for i in range(len(list)):
    list[i].send_keys('admin')
time.sleep(2)
driver.find_element_by_class_name('el-button--medium').click()
time.sleep(5)
driver.find_element_by_class_name('iconkucun').click()
# list = driver.find_elements_by_class_name('text-wrap')
# list[2].click()
