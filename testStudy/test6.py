import logging

class TestLog(object):
    '''
    封装后的logging
    '''
    def __init__(self , logger = None):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level = logging.INFO)

        handler1 = logging.FileHandler(r'C:\Users\Administrator\PycharmProjects\Test\log\test.log',encoding='utf-8')
        handler1.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        handler2 = logging.StreamHandler()
        handler2.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(handler1)
        self.logger.addHandler(handler2)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        handler1.close()
        handler2.close()

    def getlog(self):
        return self.logger