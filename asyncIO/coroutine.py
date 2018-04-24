# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: coroutine.py 
@time: 2018/4/13 16:12
"""

"""
异步IO，协程(coroutine)学习,生产者-消费者模型
"""

def consumer():
    r = ''
    while True:
        n = yield r

        if not n:
            return

        print('[CONSUMER] Consuming %s...' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0

    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)

        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)

    c.close()


c = consumer()
produce(c)