# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: do_filter_map.py 
@time: 2018/5/28 10:51
"""


'''
1. 利用filter进行复杂过滤
'''


values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

lvals = list(filter(is_int, values))
print(lvals)


'''
2. 过滤工具itertools.compress()
'''
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

counts =  [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))


'''
3.过滤，从字典中提取子集两种方法
3.1：方法一
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)


'''
3.2 方法2
'''
p1_1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1_1)
p2_1 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2_1)