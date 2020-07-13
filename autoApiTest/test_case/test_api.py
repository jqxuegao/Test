import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\Test\autoApiTest')
import pytest
from data.data import ReadExcel
from common.request import Request


testData = ReadExcel().get_course_data()

@pytest.mark.parametrize('address,api,request_mode,request_data,expected',testData)
def test_api1(address,api,request_mode,request_data,expected):
    assert Request.request(address,api,request_mode,request_data) == expected