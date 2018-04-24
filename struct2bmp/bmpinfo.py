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
@file: bmpinfo.py
@time: 2018/3/6 13:48
"""

'''
检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
'''

'''
位图分析
windows的位图文件(.bmp)是一种非常简单的文件格式，用struct分析一下。
	读入前30个字节来分析：
	>>> s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
	BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
	两个字节：'BM' 表示windows位图，'BA'表示OS/2位图；
	一个4字节整数：表示位图大小
	一个4字节整数：保留位，始终为0
	一个4字节整数：实际图像的偏移量
	一个4字节整数：Header的字节数
	一个4字节整数：图像宽度
	一个4字节整数：图像高度
	一个2字节整数：始终为1
	一个2字节整数：颜色数
  组合起来用unpack读取
  >>> struct.unpack('<ccIIIIIIHH', s)
 (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
 牛志杰
'''

import struct

# 把一个图片转换二进制数据
with open(r'pic.bmp', 'rb') as f:
    bmp_bs = f.read()


# print(bmp_bs)


# 检查bmp_bs是否是位图文件，如果是则输出图片大小和颜色数
def bmp_info(data):
    result = struct.unpack('<ccIIIIIIHH', data[:30])
    if result[0] == b'B' and result[1] == b'M':
        return {
            'width': result[6],
            'height': result[7],
            'color': result[9]
        }


# 输出

if __name__ == '__main__':
    # 检查图片
    bi = bmp_info(bmp_bs)
    print(bi, type(bi))
