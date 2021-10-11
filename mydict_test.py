import unittest

from mydict import Dict


# 编写一个测试类，从unittest.TestCase继承。

# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

class DictTest(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1,b='Test')
        self.assertEqual(d.a,1)     # 断言d.a与1相等
        self.assertEqual(d.b,'Test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # 以下两个方法会在每个测试方法执行前后运行，比如连接/关闭数据库，不必在每个测试方法重复写
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# 编写好后在最后加这两句来运行单元测试：
if __name__ == '__main__':
    unittest.main()

'''
运行方法：加上上述两句然后执行python3 ./mydict_test.py
方法二：通过参数-m unittest直接运行单元测试（推荐）

结果：Ran 5 tests in 0.001s

OK
'''