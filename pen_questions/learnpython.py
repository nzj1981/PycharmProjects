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


print(get_sum(3, 5))

print('奖金发放*****************************************')

'''
02.
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

print('\n一个整数，它加上100后是一个完全平方，再加上168又是一个完全平方，请问该数是多少？')
'''
03. 一个整数，它加上100后是一个完全平方，再加上168又是一个完全平方，请问该数是多少？
程序分析：
假设该数是x。
1.则：x + 100 = n2， x + 100 + 168 = m2
2.计算公式：m2 - n2 = ( m + n )(m - n) = 168
3.设置： m + n = i, m - n = j, i * j = 168, i 和 j 至少一个是偶数
4.可得：m = (i + j) / 2, n = (i - j) / 2 , i 和 是要么都是偶数，要么都是奇数
5.从3和4推导可知道，i与j均是大于等于2的偶数。
6.由于 i * j = 168， j >= 2,则1< i < 168 / 2 + 1
7.接下来将i的所有数字循环计算即可
'''
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print('该整数为：', x)

print('\n著名的斐波拉契数列应用*****************************')
'''
04.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后
每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？（单位：对）
程序分析：兔子的规律为数列：1, 1, 2, 3, 5, 8, 13, 21, 34, 55.....
这个题就是著名的斐波拉契数列(Fibonacci),除了第一个和第二个数外，任意一个数都可由前
两个数相加得到。
那么我们求第十个月兔子总数是多少对。
'''


def get_total_month(month):
    n, a, b = 0, 0, 1
    while n < month:
        print('第{}个月，兔子总数为：{}对'.format(n + 1, b))
        a, b = b, a + b
        n += 1
    return ''

get_total_month(10)
