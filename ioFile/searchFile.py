#!/usr/bin/env python3 
# encoding: utf-8  

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: searchFile.py 
@time: 18-2-7 下午2:47
"""
'''
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

os.walk(top, topdown=True, onerror=None, followlinks=False)
top 是你所要便利的目录的地址
topdown 为真，默认优先遍历top目录
onerror 需要一个callable对象，当walk需要异常时，会调用
followlinks 如果为真，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指
的目录(默认关闭)
os.walk的返回值是一个生成器(generator)，也就是说我们需要不断的遍历它，来获得所有的内容
每次遍历的对象都是返回的是一个三元组（root, dirs, files)
topdown参数为真， walk会遍历top文件夹，与top文件夹中每一个子目录
方法一：
'''

import os

def searchFile(str, path='.'):
    for root, dirs, files in os.walk(path):
        for f in files:
            fPath = os.path.join(root, f)
            if str in f:
                # 相对路径
                # print(fPath)
                # 绝对路径
                print(os.path.abspath(fPath))

'''
方法二：
递归实现法：遇到文件夹用递归实现查找
'''
print('-------------------分割线------------------------')

def findFile(str, path='.'):
    for f in os.listdir(path):
        fPath = os.path.join(path, f)
        if os.path.isfile(fPath) and str in f:
            print(fPath)
        if os.path.isdir(fPath):
            findFile(str, fPath)
        '''
        注意isfile（fpath）和isdir（fpath）的参数默认为当前目录，
        写相对路径或绝对路径，不要只写个文件名，避免递归查询时找不到子目录的文件
        '''

if __name__ == '__main__':
    searchFile('searchFile.py')
    findFile('findFile.py')