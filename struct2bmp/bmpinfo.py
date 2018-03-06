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
