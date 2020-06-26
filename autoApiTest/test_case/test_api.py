import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\Test\autoApiTest')
import pytest
from data.data import ReadExcel
from common.request import Request



def get_course_data():
    testData = ReadExcel().read_excel()
    course_data = []
    for apidata in testData:
        address = apidata['地址']
        api = apidata['接口']
        request_mode = apidata['请求方式']
        request_data = apidata['请求内容']
        expected = apidata['断言']
        course_data.append((address,api,request_mode,request_data,expected))
    return course_data

testData = get_course_data()

@pytest.mark.parametrize('address,api,request_mode,request_data,expected',testData)
def test_api1(address,api,request_mode,request_data,expected):
    assert Request.request(address,api,request_mode,request_data) == expected