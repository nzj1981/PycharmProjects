# !/usr/bin/env python3
# coding=utf-8

'''

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
***返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**
example:
利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''


# 方法一 利用生成器实现计数器
# def createCounter():
#     def f():
#         n = 0
#         while True:
#             n += 1
#             yield n
#     sun = f()
#     def counter():
#         return next(sun)
#     return counter

# 方法二使用列表（列表list是全局变量，创建一个只有一个元素的列表
# def createCounter():
#     fs = [0]
#
#     def counter():
#         fs[0] += 1
#         return fs[0]
#
#     return counter

# 方法三使用nonlocal关键字将局部变量变成全局变量
def createCounter():
    n = 0

    def counter():
        nonlocal n
        n += 1
        return n

    return counter


# 测试
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试成功')
else:
    print('测试失败')
