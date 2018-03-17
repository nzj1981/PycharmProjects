#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: getZhishu.py 
@time: 2018/3/17 16:53
"""
'''
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果
输入值满足3<= n < 1000)

例如：
如果输入为10，程序应该输出结果为1.(共有1对质数的和为10，分别为(3, 7))
'''
from math import sqrt

# 假定n = 10
def get_total_couple(n):
    # 判定输入值满足3<= n < 1000
    if n < 3 or n >= 1000:
        raise 'Input out of given range!'

    # 定义一个统计变量
    count = 0
    x = 0
    lst = []

    # 决定2~n内数字是否是质数
    def if_a_zhishu(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # 把3~n范围内的质数追加到lst列表中
    for j in range(3, n + 1):
        if if_a_zhishu(j):
            lst.append(j)

    # 把两对质数和为n,统计出来。
    print(lst)
    for item in lst:
        x = n - item
        if x in lst:
            count += 1
            print(x, item)
            lst.remove(item)

    return count

# 测试
print(get_total_couple(100))

