import xlrd
from autoApiTest.config.readconfig import ReadConfig

class ReadExcel():

    def __init__(self):
        self.data = ReadConfig()

    def read_excel(self):
        excel_address = self.data.get_address()
        table = xlrd.open_workbook(excel_address).sheet_by_index(0)
        body_data = {} # 空字典，用于存放每一组数据
        body_loop = 1
        while True:
            for i in range(table.ncols):
                # table.cell(0,i).value : 把第一行的每一列当成字典的key
                # table.cell(body_loop,i).value ：从第二行开始，每一列的值作为字典key对应的值
                body_data[table.cell(0,i).value] = table.cell(body_loop,i).value #获取一组数据
            body_loop += 1
            if body_loop >= table.nrows:   #大于表格的总行数就退出循环
                break
        return body_data

if __name__ == '__main__':
    print(ReadExcel().read_excel())
