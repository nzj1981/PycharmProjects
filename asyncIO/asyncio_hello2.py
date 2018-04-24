# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: asyncio_hello2.py 
@time: 2018/4/18 9:47
"""

'''
为了简化并更好地标识异步IO，自python3.5引入新语法async和wait，
可以让coroutine的代码更简洁易读。
如何替换：
1.把@asyncio.coroutine替换为async
2.把yield from 替换为await
'''

import threading
import asyncio



async def hello():
    print('Hello world! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()