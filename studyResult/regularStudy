import re

def re_test(test):
    if re.match(r'^\d{3}\-\d{3,8}$',test):
        print('ok')
    else:
        print('no')

re_test('010-12345')

def re_test1(test1):
    return re.split(r'\s',test1)

print(re_test1('a b  c'))

def re_test2(test1):
    return re.split(r'\s+',test1)

print(re_test2('a b  c'))


def re_test3(test1):
    return re.split(r'[\s\,]+',test1)

print(re_test3('a,b, c  d'))

def re_test4(test1):
    return re.split(r'[\s\,\;]+',test1)

print(re_test4('a,b,;;c  d'))

def re_test5(test1):
    m = re.match(r'^(\d{3})-(\d{3,8})$',test1)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

re_test5('010-12345')