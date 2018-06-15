# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: deduplication_list_dict.py 
@time: 2018/5/23 10:21
"""


'''
删除序列相同元素并保持顺序
'''


# 去除列表重复元素并保持顺序
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 2, 5, 1, 8, 1, 5, 10]
print(list(dedupe(a)))


# 去除列表中重复的字典元素
def dedupDict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


l = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4}
]

print(list(dedupDict(l, key=lambda d: (d['x'], d['y']))))
print(list(dedupDict(l, key=lambda d: d['x'])))


# 仅消除重复值不考虑顺序，可通过集合实现
b = [1, 2, 1, 3, 5, 10, 9, 5]
print(set(b))


# 去除文件中重复行
with open('deque_text.txt') as f:
    for line in dedupe(f):
        print(line)


