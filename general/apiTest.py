import requests
import xlrd

print("hello world")
print("hello xuegao")

def getRun():
    url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?'
    data = xlrd.open_workbook('C:\\Users\\46362\\Desktop\\test.xlsx')
    table = data.sheets()[0] # 打开第一张表
    print (table.name) # 获取sheet名称
    print (table.ncols) # 获取总列数
    print (table.nrows) # 获取总行数
    rows = table.nrows

    for i in range(rows):
        params = {
            'tel':table.row_values(i)
        }
        response = requests.get(url,params)
        print(response.text)

getRun()




def postRun():
    url = ''
    headers = {


    }
    response = requests.post(url,headers)
