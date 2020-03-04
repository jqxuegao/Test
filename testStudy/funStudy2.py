
def p():
    '''i()返回的是一个元组类型的'''
    print(i()[0])

def i():
    a = input("a:")
    b = input("b:")
    return a,b



p()
