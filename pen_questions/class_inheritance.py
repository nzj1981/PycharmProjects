# !/usr/bin/env python3.6
# coding=utf-8


class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('derived show')

obj = B()

obj.show()

# 1.Q:如何调用类A的show方法

# A:__class__方法指向了类对象，只用给他赋值类型A，然后调用方法show。用完要修改回来
obj.__class__ = A
obj.show()

def decToBOH(a, b):
    s = set()
    s = {'2', '8', '16'}
    if str(b) not in s:
        print('errors')
        exit()
    z = ''
    if str(a).isdigit():
        x = a
        while True:
            if x == 0:
                break
            y = x % b
            x = x // b
            z = str(y) + z
    return z
print(decToBOH(10, 2))

def findMinAndMax(L):
    mx, mn = (None, None)
    if len(L) != 0:
        t = tuple(L)
        mx = max(t)
        mn = min(t)
    return (mn, mx)
print(findMinAndMax([7,3]))

def triangles():
    n = 0
    l = [1]
    while 1:
        yield l
        l = [l[x] + l[x + 1] for x in range(n)]
        l.insert(0, 1)
        l.append(1)
        n += 1
    return l

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
a=[1]
a[]