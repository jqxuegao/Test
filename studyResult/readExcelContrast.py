import pandas
import operator

def excel_one_line_to_list1():
    df = pandas.read_excel(r"C:\Users\Administrator\Desktop\优托邦\缺失面积--测试版2.xlsx", usecols=[53],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

def excel_one_line_to_list2():
    df = pandas.read_excel(r"C:\Users\Administrator\Desktop\优托邦\缺失面积--测试版2.xlsx", usecols=[54],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    return result

if __name__ == '__main__':
    #对比两列是否完全一致
    #可以修改函数进行数据库和excel进行对比
    print(operator.eq(excel_one_line_to_list1(), excel_one_line_to_list2()))
