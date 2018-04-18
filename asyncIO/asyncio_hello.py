# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: asyncio_hello.py 
@time: 2018/4/13 16:27
"""

"""
asyncio 异步io的用法
"""

import threading
import asyncio

# @asyncio.coroutine是把一个generator标记为coroutine类型,然后把这个coroutine放到EventLoop执行
@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.current_thread())


# 获取EventLoop
loop = asyncio.get_event_loop()

# 执行coroutine

loop.run_until_complete(hello())

loop.close()