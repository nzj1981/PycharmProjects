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
"""

import asyncio


def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect

    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()

    while True:
        line = yield from reader.readline()

        if line == b'\r\n':
            break

        print('%s header > %s' % (host, line.decode('utf-8').rsplit()))

    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
