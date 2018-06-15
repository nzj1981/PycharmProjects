# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: sorted_max_min.py
@time: 2018/5/22 10:52
"""


'''
1.从一个集合中获得最大或最小的N个元素
'''


import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))



'''
两个函数都可以接受关键字参数
'''
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
print(cheap)
print(expensive)


# 2.实现一个优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]



class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)


print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())


# 3.在数据字典中执行计算操作，如：求最小值、最大值或排序等
# zip函数将键和值反转,zip函数一个只能访问一次的迭代器,sorted函数用来排序
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 4.sorte
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)


'''
5.通过某个关键字排序一个字典列表
利用operator模块中itemgetter函数来实现
在字典列表中也可以采用min()和max()函数
min(sorted(rows, key=itemgetter('uid'))
max(sorted(rows, key=itemgetter('uid'))
'''
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'Davild', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print('按照名字进行排序：%s' % rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'), reverse=True)
print('按照UID从大到小进行排序：%s' % rows_by_uid)
rows_by_flname = sorted(rows, key=itemgetter('fname', 'lname'))
print('按照全名进行排序：%s' % rows_by_flname)


'''
6.类型相同的对象排序，但只能排序不可进行原生的比较操作
可以采用operator中r attrgetter进行操作排序
在类型对象也可以采用min()和max()函数
min(sorted(users, key=attrgetter('user_id'))
max(sorted(users, key=attrgetter('user_id'))
'''
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(2), User(99)]
print('原始对象:%s' % users)
print('对象排序:%s' % sorted(users, key=lambda u: u.user_id))
from operator import attrgetter
print('采用attrgetter方法进行对象排序:%s' % sorted(users, key=attrgetter('user_id')))


'''
7.对一个字典或者实例的序列，根据某个特定字段进行分组。
'''
lists = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/02/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
from collections import defaultdict

ls = sorted(lists, key=itemgetter('date'))
d = {}
d1 = defaultdict(list)
print('对一个字典或者实例的序列，根据某个特定字段进行分组')
for date, items in groupby(ls, key=itemgetter('date')):
    print(date)
    for i in items:
        print('  ', i)
        d.setdefault(date, []).append(i)
        d1[date].append(i)
print(d)
print(d1)