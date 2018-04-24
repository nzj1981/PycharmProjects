# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: asynicio_wget.py 
@time: 2018/4/13 16:41
"""

"""
利用asyncio的异步网络连接来获取sina,sohu,163的网站的首页

为了简化并更好地标识异步IO，自python3.5引入新语法async和wait，
可以让coroutine的代码更简洁易读。
如何替换：
1.把@asyncio.coroutine替换为async
2.把yield from 替换为await
"""

import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect

    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line = await reader.readline()

        if line == b'\r\n':
            break

        print('%s header > %s' % (host, line.decode('utf-8').rsplit()))

    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
