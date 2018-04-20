# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: faq.py 
@time: 2018/4/20 11:57
"""
# 1.获取当前路径
# 当前路径可以用"."表示,再用os.path.abspath()将其转换为绝对路径.
import os

print('1.current directory:', os.path.abspath('.'))


# 2.获取当前模块文件名
print('2.current abspath file name:', __file__)
print('2.1.current file name:', os.path.basename(__file__))


# 3.获取命令行参数
import sys

if len(sys.argv) >= 2:
    print('3.current parameters: %s' % sys.argv)
else:
    print('3.no input parameter')


# 4.获取当前python命令的可执行文件路径
print('current python command executable path: %s' % sys.executable)