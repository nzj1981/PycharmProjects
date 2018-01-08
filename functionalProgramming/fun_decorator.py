# !/usr/bin/env python3
# coding = utf-8
'''
装饰器(decorator)是一个高阶函数
在函数调用前后自动打印日志，但又不希望修改本身函数的定义，这种在代码运行期间动态增加功能的方式，称为“装饰器”(decorator)

'''
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}():'.format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2018-01-08')


now()


def logger(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('{} call {}():'.format(text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2018-01-08')


today()
