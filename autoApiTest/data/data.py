import sys
sys.path.append(r'C:\Users\Administrator\PycharmProjects\Test\autoApiTest')
import xlrd
from config.readconfig import ReadConfig

class ReadExcel():

    def __init__(self):
        self.data = ReadConfig()

    def read_excel(self):
        excel_address = self.data.get_address()
        table = xlrd.open_workbook(excel_address).sheet_by_index(0)
        body_list =[]
        body_loop = 1
        while True:
            body_data = {} # 空字典，用于存放每一组数据
            for i in range(table.ncols):
                # table.cell(0,i).value : 把第一行的每一列当成字典的key
                # table.cell(body_loop,i).value ：从第二行开始，每一列的值作为字典key对应的值
                body_data[table.cell(0,i).value] = table.cell(body_loop,i).value #获取一组数据
            body_list.append(body_data)
            body_loop += 1
            if body_loop >= table.nrows:   #大于表格的总行数就退出循环
                break
        return body_list


    def get_course_data(self):
        testData = self.read_excel()
        course_data = []
        for apidata in testData:
            address = apidata['地址']
            api = apidata['接口']
            request_mode = apidata['请求方式']
            request_data = apidata['请求内容']
            expected = apidata['断言']
            course_data.append((address,api,request_mode,request_data,expected))
        return course_data


if __name__ == '__main__':
    print(ReadExcel().read_excel())
    print(ReadExcel().get_course_data())
