
def div(a,b):
    try:
        # 执行代码
        print(a/b)
    except:
        print("发生异常")
    else:
        print("没有异常执行的代码")
    finally:
        print('不管有没有异常，都执行的代码')

div(1,0)