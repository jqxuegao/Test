from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
driver.find_element_by_class_name('lnk-movie').click()
time.sleep(5)
driver.implicitly_wait(10)
a = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[4]/a').click()
# driver.find_element_by_xpath('//*[@id="douban-top250"]/div[1]/h2/span/a').click()
#
# movie = driver.find_element_by_class_name('grid_view')
# len(movie)





