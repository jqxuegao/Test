import xlrd

def doExl():

    # 打开文件
    data = xlrd.open_workbook(r'C:\Users\46362\Desktop\滴普\test.xls')
    # 打开第一张sheet1表
    table = data.sheets()[0]
    # 获取sheet名称
    print ("sheet名称：",table.name)
    # 获取总列数
    print ("总列数：",table.ncols)
    # 获取总行数
    print ("总行数：",table.nrows)
    # 获取第三行，第二列值
    value1 = table.cell(2,1).value
    # 打印
    print("第三行，第二列值:",value1)

doExl()