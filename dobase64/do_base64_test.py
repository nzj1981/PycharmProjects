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
@file: do_base64_test.py 
@time: 2018/3/6 9:26
"""

# 测试

import unittest
from do_base64 import safe_base64_decode

class Test_safe_base64_decode(unittest.TestCase):
    def test_init(self):
        bs = safe_base64_decode(b'YWJjZA==')
        self.assertEqual(bs, b'abcd')
        self.assertTrue(isinstance(bs, bytes))

        bs1 = safe_base64_decode(b'YWJjZA')
        self.assertEqual(bs1, b'abcd')
        self.assertTrue(isinstance(bs1, bytes))

if __name__ == '__main__':
    unittest.main()