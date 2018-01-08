# !/usr/bin/env python3
# coding= utf-8

'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
要求：
1.请用sorted()对上述列表分别按名字排序：
2.请按成绩从高到低排序：
'''

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 方法一：
def by_name(t):
    return t[0]


print('方法一，按名字排序：', sorted(L, key=by_name))


def by_score(t):
    return t[1]


print('方法一，按成绩倒序：', sorted(L, key=by_score, reverse=True))

# 方法二
print('方法二，按名字排序：', sorted(L, key=lambda x: x[0]))

print('方法二，按成绩排序：', sorted(L, key=lambda x: x[1], reverse=True))

# 方法三
from operator import itemgetter

print('方法三，按名字排序：', sorted(L, key=itemgetter(0)))

print('方法三，按成绩排序：', sorted(L, key=itemgetter(1), reverse=True))