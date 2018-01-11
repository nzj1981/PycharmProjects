# !/usr/bin/env python3
# coding = utf-8

'''
多重继承是python特有继承，很多编程语言都是单根单向继承,意思就是子类只能有一个父类,
而且是单一方向的,不能子类继承父类,父类继承该子类;
在Python中,继承功能更加的强大,支持Mixin,就是混合继承,一个子类可以同时继承多个父类,
而不是一级一级的继承;但是Mixin这个功能在某些语言中是通过协议来完成的,
遵循某个协议就拥有了协议里定义的方法,跟Mixin有相似的用处.
example：
实现MixIn继承的顺序关系
'''
import inspect


class G(object):
    pass


class D(object):
    def __init__(self):
        print('D')


class E(object):
    def __init__(self):
        print('E')


class F(object):
    def __init__(self):
        print('F')


class C(D, F):
    def __init__(self):
        print('C')


class B(E, G):
    def __init__(self):
        print('B')


class A(B, C):
    def __init__(self):
        print('A')


# 测试

if __name__ == '__main__':
    print(inspect.getmro(A))
