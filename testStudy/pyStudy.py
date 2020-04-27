from selenium import webdriver
from ddt import ddt,data
import unittest
import time

@ddt
class A(unittest.TestCase):

    @data('1','2')
    def test_b(self,a):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(a)
        driver.find_element_by_id('su').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
