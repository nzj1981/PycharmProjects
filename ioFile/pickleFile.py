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
@file: pickleFile.py 
@time: 2018/2/12 15:24
"""

import json

'''
例子：对中文进行JSON序列化，json.dumps()提供了一个ensure.ascii参数，该参数对结果的影响是什么？
'''

obj = dict(name='小明', age=20)

s = json.dumps(obj, ensure_ascii=True)

print(s)

# s反序列化
print(json.loads(s, encoding='gb2312'))
