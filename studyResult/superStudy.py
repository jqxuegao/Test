class A():
    def __init__(self):
        print('begin a')
        print('end a')

class B(A):
    def __init__(self):
        print('begin b')
        super().__init__()
        print('end b')

class C(A):
    def __init__(self):
        print('begin c')
        super().__init__()
        print('end c')

class D(B,C):
    def __init__(self):
        print('begin d')
        super().__init__()
        print('end d')

a = D()

print('----------------------')

class A:
    def add(self,a,b):
        print(a+b)

class B(A):
    def p(self):
        super().add(3,4)


b = B()
b.p()