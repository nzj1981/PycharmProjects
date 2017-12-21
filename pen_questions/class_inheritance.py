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

# Q:如何调用类A的show方法

# A:__class__方法指向了类对象，只用给他赋值类型A，然后调用方法show。用完要修改回来
obj.__class__ = A
obj.show()
