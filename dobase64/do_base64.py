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
@file: do_base64.py.py 
@time: 2018/3/6 9:22
"""

'''
写一个能处理掉=的base64解码函数
'''

import base64


def safe_base64_decode(s):
    while len(s) % 4 != 0:
        if isinstance(s, bytes):
            s += b'='
    return base64.b64decode(s)
