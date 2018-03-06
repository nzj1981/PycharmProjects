# !/usr/bin/env python3
# coding=utf-8

import unittest

from mydict import Dict

'''
引入python自带unittest模块,进行单元测试
以test开头的方法就是测试方法
1.assertEqual  断言函数返回的结果是否相等
2.assertTrue   断言函数返回的结果是否为真
3.with self.assertRaise(KeyError): 期待抛出指定类型的Error

运行单元测试方法：
1)当做正常python脚本运行
python3 mydict_test.py
2)命令行通过参数-m unittest直接运行单元测试
python3 -m unittest mydict_test.py

在单元测试中有两个特殊的setUp()和tearDown()方法，这两个方法会分别在每调用一个测试方法的前后
分别被执行。
例子：setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样不必在每个测试方法中重复相同代码。

'''


class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        # self.assertTrue('key' not in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()

        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()

        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print('tearDown...')






if __name__ == '__main__':
    unittest.main()
