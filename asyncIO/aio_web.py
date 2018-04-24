# encoding: utf-8

__author__ = 'autumner'

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: aio_web.py 
@time: 2018/4/18 16:22
"""

"""
asyncio实现了TCP,UDP,SSL等协议，aiohttp则是基于asyncio
实现的HTTP框架
--服务端的单线程+coroutine实现多用户的高并发支持
async web application
"""

import asyncio
from aiohttp import web


# page index
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index page</h1>', content_type='text/html')


# page content
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text_html')


# page init
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


# asyncio main
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
