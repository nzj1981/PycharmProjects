# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: grepFile.py 
@time: 2018/7/24 10:44
"""
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
    查找目录树中与shell通配符模式匹配的所有文件名
    :param filepat:
    :param top:
    :return:
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
    一次打开一个文件名序列，生成文件对象。
    进行下一次迭代时，文件立即关闭。
    :param filenames:
    :return:
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
    将一系列迭代器链接在一起形成一个序列。
    :param iterators:
    :return:
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
    在一系列行中查找正则表达式模式
    :param pattern:
    :param lines:
    :return:
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line



'''
usage:
>>> import grepFile as gf
>>> filenames = gf.gen_find('dmesg*', '/var/log')
>>> files = gf.gen_opener(filenames)
>>> lines = gf.gen_concatenate(files)
>>> dmesglines = gf.gen_grep('(?i)EXT4-fs', lines)
>>> for line in dmesglines:
...     print(line)
... 
EXT4-fs (dm-0): INFO: recovery required on readonly filesystem

EXT4-fs (dm-0): write access will be enabled during recovery

EXT4-fs (dm-0): orphan cleanup on readonly fs

EXT4-fs (dm-0): ext4_orphan_cleanup: deleting unreferenced inode 393363

EXT4-fs (dm-0): ext4_orphan_cleanup: deleting unreferenced inode 393368
...
'''