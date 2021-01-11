import sys, os
sys.path.append(os.pardir)
import pytest
from autoApiTest.data.data import ReadExcel
from autoApiTest.common.request import Request


testData = ReadExcel().get_course_data()

@pytest.mark.parametrize('address,api,request_mode,request_data,expected',testData)
def test_api1(address,api,request_mode,request_data,expected):
    assert Request.request(address,api,request_mode,request_data) == expected