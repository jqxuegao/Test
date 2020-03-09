Unittest：

TestCase：测试用例
TestSuit：测试集
TestLoader：加载用例
TextTestRunner：执行用例
HTMLTestRunnerNew：推荐使用，生成HTML网页版测试报告

assertEqual(a,b，[msg='测试失败时打印的信息'])： 断言a和b是否相等，相等则测试用例通过。

assertNotEqual(a,b，[msg='测试失败时打印的信息'])： 断言a和b是否相等，不相等则测试用例通过。
assertTrue(x，[msg='测试失败时打印的信息'])： 断言x是否True，是True则测试用例通过。
assertFalse(x，[msg='测试失败时打印的信息'])： 断言x是否False，是False则测试用例通过。
assertIs(a,b，[msg='测试失败时打印的信息'])： 断言a是否是b，是则测试用例通过。
assertNotIs(a,b，[msg='测试失败时打印的信息'])： 断言a是否是b，不是则测试用例通过。
assertIsNone(x，[msg='测试失败时打印的信息'])： 断言x是否None，是None则测试用例通过。
assertIsNotNone(x，[msg='测试失败时打印的信息'])： 断言x是否None，不是None则测试用例通过。
assertIn(a,b，[msg='测试失败时打印的信息'])： 断言a是否在b中，在b中则测试用例通过。
assertNotIn(a,b，[msg='测试失败时打印的信息'])： 断言a是否在b中，不在b中则测试用例通过。
assertIsInstance(a,b，[msg='测试失败时打印的信息'])： 断言a是是b的一个实例，是则测试用例通过。
assertNotIsInstance(a,b，[msg='测试失败时打印的信息'])： 断言a是是b的一个实例，不是则测试用例通过。。

setUp函数：初始化环境（执行每条用例之前，都要执行setUp函数下面的代码，每次都要执行）
tearDown函数：清洗环境（执行每条用例之后，都要执行tearDown函数下面的代码，每次都要执行）


setup():每个测试case运行前运行
teardown():每个测试case运行完后执行
setUpClass():必须使用@classmethod 装饰器,所有case运行前只运行一次
tearDownClass():必须使用@classmethod装饰器,所有case运行完后只运行一次


