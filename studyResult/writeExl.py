import xlwt

def do_input():
    a = input("输入的值填入到excel：")
    return a

def do_excel():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('hello xlwt')
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0, 0, label = do_input()[0:100])
    # 保存
    workbook.save(r'C:\Users\46362\Desktop\滴普\test.xls')

do_excel()