# 把一个函数作为传参，传给修饰器
def hello(func):

    def hello1():
        # 内嵌函数，给传入的函数进行修饰
        print('hello头部修饰')
        func()
        print('hello尾部修饰')
    # 修饰完，返回出去
    return hello1

def hi(func):

    def hi1():
        print('hi头部修饰')
        func()
        print('hi尾部修饰')

    return hi1

# 调用修饰器，修饰下面的函数
# 哪个先调用，哪个先修饰
@hi
@hello
def c():
    print("我被修饰了")

# 修饰完的调用
c()