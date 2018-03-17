#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: learnpython.py 
@time: 2018/3/17 20:27
"""

'''
01.求s = a + aa + aaa + aaaa + aaaaa +aa...a的值，其中a是一个数字。
例如：
2 + 22 + 222 + 2222 + 22222(此时共有5个数相加),几个数相加由键盘控制 
'''
from functools import reduce

# 利用高阶函数reduce的累积计算
print('一个重复n次数字的序列相加*************************')


def get_sum(a, n):
    tn = 0
    lst = []

    for i in range(n):
        tn = tn * 10 + a
        lst.append(tn)
    # print(list(map(str, lst)))
    l = list(map(str, lst))
    for i in l:
        if l.index(i) < len(l):
            print(i, '+ ', end='')
    print(l[-1], ' = ', end='')
    return reduce(lambda x, y: x + y, lst)


print(get_sum(2, 3))

print('奖金发放*****************************************')

'''
企业发放的奖金根据利润提成。
1.利润(I)低于或等于10万元时，奖金可提10%；
2.利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
3.20万元到40万元之间时，高于20万元的部分，可提成5%；40万元到60万元之间时高于40万元的部分，可提成3%；
4.60万元到100万元之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成；
从键盘输入当月利润I，求应发放奖金总数。
'''


def cal_bonus(profit):
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0

    for idx in range(6):
        if profit > arr[idx]:
            r += (profit - arr[idx]) * rat[idx]
            print(idx, ':', profit, '{} = {} * {}'.format(r, (profit - arr[idx]),
                  rat[idx]))

            profit = arr[idx]

    return '总计奖金：' + str(r)


print(cal_bonus(1000000))
