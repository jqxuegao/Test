import unittest,ddt
from autoApiTest.data.data import ReadExcel
from autoApiTest.common.request import Request

testData = ReadExcel().read_excel()

@ddt.ddt
class Api(unittest.TestCase):

    @ddt.data(*testData)
    def test_1(self,data):
        # print(data)
        re = Request().request(data)
        # print(re)
        self.assertEquals(re,200)

if __name__ == '__main__':
    unittest.main()