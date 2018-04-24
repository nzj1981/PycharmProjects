# !/usr/bin/env python3
# encoding: utf-8
# set(  = "https://github.com/nzj1981/PycharmProjects.git" )

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site:  
@software: PyCharm 
@file: toTimestamp_test.py 
@time: 2018/3/5 13:48
"""

import unittest
from toTimestamp import to_timestamp

'''
针对to_timestamp函数进行单元测试
'''

class Test_to_timestamp(unittest.TestCase):
    def test_init(self):
        t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
        self.assertEqual(t1, 1433121030.0)
        self.assertTrue(isinstance(t1, float))

        t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
        self.assertEqual(t2, 1433121030.0)
        self.assertTrue(isinstance(t2, float))

if __name__ == '__main__':
    unittest.main()