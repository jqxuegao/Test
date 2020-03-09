import unittest
from demo import add,div

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有case运行前只运行一次")

    @classmethod
    def tearDownClass(cls):
        print("所有case运行完后只运行一次")

    def setUp(self):
        print("每条case运行前运行一次")

    def tearDown(self):
        print("每条case运行完后运行一次")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))

    def test_div(self):
        self.assertEqual(3,div(3,1))
        self.assertNotEqual(3,div(2,1))

    @unittest.skip('不准备跑')
    def test_add_with_skip(self):
        self.assertEqual(1, add(3, 2))
        self.assertNotEqual(1, add(3, 2))

    # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
    # 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
        unittest.main(verbosity=1)