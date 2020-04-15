import unittest
from selenium import webdriver
from ddt import ddt,data

@ddt
class TestA(unittest.TestCase):

    @data('cjq','czl')
    def test_A(self,txt):
        driver = webdriver.Chrome()
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(txt)
        driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()