# 第一种
# 函数括号为调用该函数必须传值，个数必须一致，而且必须一一对应
def a(length,width):
    return length * width

print(a(5,6))

print('-----------------------------')
# 第二种
# 初始化默认值
def b(length,width=3):
    return length * width
print(b(2))
print(b(3,5))

print('-----------------------------')
# 第三种
# 多个不确定传参
def c(*legth):
    if len(legth) == 0:
        print('长度为0')
    else:
        print(legth)
#存放在元组中
c()
c(1)
c(1,2,3)

print('-----------------------------')
# 第四种
#多个不确定的参数，必须以字典的方式存入
def d(**legth):
    if len(legth) == 0:
        print('长度为0')
    else:
        print(legth)
d(a=1)
#不以字典为格式就报错
d(a)