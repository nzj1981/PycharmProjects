#!/usr/bin/env python3
# encoding: utf-8  

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: findFile.py 
@time: 18-2-7 下午1:39 
"""
'''
利用os模块编写怀个能实现dir -l输出的程序
'''
import os
import time
'''
localtime():格式化时间戳(最后一次修改时间)为本地时间
strftime()：接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定

'''

def dir_l(path = '.'):
    print('最后修改时间\t\t\t大小\t\t文件名')
    print('-----------------------------------------')
    for f in os.listdir(path):
        fsize = os.path.getsize(os.path.join(path, f))
        st = os.stat(os.path.join(path, f))
        mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(st.st_mtime))
        print('%s\t\t%5d B\t\t%s' % (mtime, fsize, f))

if __name__ == '__main__':
    dir_l('/home/autumn/python_source/PycharmProjects')
