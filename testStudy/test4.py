import pandas

def excel_one_line_to_list1():
    df = pandas.read_excel(r"C:\Users\Administrator\Desktop\优托邦\缺失面积--测试版2.xlsx", usecols=[53],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

