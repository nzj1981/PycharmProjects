# !/usr/bin/env python3
# coding=utf-8
'''
1.利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

'''
from functools import reduce

def str2float(s):
    def char2num(s):
        CHAR_TO_FLOAT = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        return CHAR_TO_FLOAT[s]
    l, r = [0, 0]
    if '.' in s:
        left, right = s.split('.')
        if left is '0' or left is '':
            l = 0
        else:
            l = reduce(lambda x, y: x * 10 + y, map(char2num, left))
        if right is '0' or right is '':
            r = 0
        else:
            r = reduce(lambda x, y: x * 10 +y, map(char2num, right)) / pow(10, len(right))
    else:
        left = s
        l = reduce(lambda x, y: x * 10 + y, map(char2num, left))
    return l + r



print(str2float('123.456'))
print(str2float('0'))
print(str2float('123.456000'))
print(str2float('.1234'))
print(str2float('120.0034'))

'''
2.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['admin', 'LISA', 'barT']，
输出：['Admin', 'Lisa', 'Bart']
'''
print('2.******************************************')
list1 = ['admin', 'LISA', 'barT']
def normalize(name):
    return name.capitalize()
    # same as return name.title()
print(list(map(normalize, list1)))
'''
3.Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce
求积：
'''
print('3.******************************************')
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('\"[1, 3, 5]的乘积为\"：', prod([1, 3, 5]))