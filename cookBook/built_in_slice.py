# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: built_in_slice.py 
@time: 2018/5/23 11:21
"""


'''
内置slice()函数被用在任何切片允许使用的地方
1.slice常见用法
2.切片的属性start, stop, step
3.indices(size)方法将它映射到一个确定大小的序列上
'''
items = [0, 1, 2, 3, 4, 5, 6]
sli = slice(2, 4)
print(items[2:4])
print(items[sli])

print('原items:', items)
items[sli] = [10, 11]
print('变化后items:', items)

del items[sli]
print('删除切片后的items', items)

print('切片属性---start, stop, step')
a = slice(5, 50, 2)
print('a.start:%d, a.stop:%d, a.step:%d' % (a.start, a.stop, a.step))


print('indices方法使用')
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])