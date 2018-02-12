#!/usr/bin/env python3 
# encoding: utf-8  

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: strIoFile.py 
@time: 18-2-12 上午11:32
"""
from io import StringIO
from io import BytesIO


# StringIO和BytesIO

# stringIO只需要对数据进行操作，并把数据存储在本地磁盘上可以使用StringIO

def outputstring():
    return 'string \nfrom \noutputstring \nfunction'


s = outputstring()

# 将函数返回到数据在内存中读

sio = StringIO(s)
# 可使用StringIO自身的方法
print(StringIO.getvalue(sio))

# 也可以使用file-like object的方法
print('--------------readlines()读取内存数据--------------------------------')
s = sio.readlines()
for i in s:
    print(i.strip())

print('----------------------将函数返回的数据写内存中-------------------------------------')
s1 = outputstring()
# 将函数返回的数据写内存中
sio1 = StringIO()
sio1.write(s1)
# 可使用StringIO自身的方法
print(sio1.getvalue())

'''
tell 方法获取当前文件读取指针的位置
seek 方法用于移动文件读写指针到指定位置，有两个参数，第一个offset：偏移量，需要向前或向后
的字节数，正为向后，负为向前；第二个whence：可选值，默认为0，表示文件开头，1表示相对于当前的位置
2表示文件末尾
用seek方法时需要注意，如果你打开文件没有用'b'的方式打开，则 offset无法使用负值
'''
print('---------------tell与seek用法-----------------------')
s2 = outputstring()
sio = StringIO()
sio.write(s2)
sio.seek(0, 0)
print(sio.tell())
for i in sio.readlines():
    print(i.strip())

'''
操作二进制数据需要用到BytesIO
同时seek就可以向前移动
'''
print('-------------------BytesIO用法------------------------')
s3 = outputstring()

bio = BytesIO()
bio.write(s3.encode('utf-8'))
print(bio.getvalue())
bio.seek(-36, 1)
print(bio.tell())
for i in bio.readlines():
    print(i.strip())
