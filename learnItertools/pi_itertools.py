#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: pi_itertools.py 
@time: 2018/3/15 13:15
"""
'''
例子：
计算圆周率可以根据公式：
利用Python提供的itertools模块，来计算这个序列的前N项和：
计算pi的值：
step 1：创建一个奇数序列：1, 3, 5, 7, 9, ...

step 2：取该序列的前N项：1, 3, 5, 7, 9, ..., 2 *N -1.

step 3: 添加正负符号并用4除： 4/1， -4/3， 4/5，-4/7，4/9，...

step 4: 求和

return 3.14
'''

import itertools


# 方法一：利用cycle函数

def pi_cycle(N):
    natuals = itertools.count(1, 2)

    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals)

    # 添加正负号
    ns_cycle = itertools.cycle([1, -1])

    ns_seq = map(lambda x: next(ns_cycle) * 4 / x, ns)

    return sum(ns_seq)


print('pi_cycle:', pi_cycle(100))


# 方法二：利用chain函数

def pi_chain(N):
    natuals1 = itertools.count(start=1, step=4)
    natuals2 = itertools.count(start=3, step=4)

    ns1 = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals1)
    ns2 = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals2)

    ns_seq1 = (4 / x for x in ns1)
    ns_seq2 = (-4 / x for x in ns2)

    return sum(itertools.chain(ns_seq1, ns_seq2))


print('pi_chain:', pi_chain(100))

# 方法三：利用数学函数pow

import math


def pi_pow(N):
    natuals = itertools.count(1, 2)
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals)

    mCount = 0
    mSum = 0

    for x in ns:
        mSum += 4 / x * math.pow(-1, mCount)
        mCount += 1

    return mSum

print('pi_pow:', pi_pow(100))