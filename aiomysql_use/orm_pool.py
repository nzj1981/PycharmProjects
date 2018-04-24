# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: orm_pool.py 
@time: 18-4-24 下午9:12
"""
__author__ = 'autumner'

'''
access mysql pool
'''

import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def go():
    global __pool
    __pool = await aiomysql.create_pool(
        host='103.231.145.114',
        port=8094,
        user='pyuser',
        password='pyuser123',
        db='awesome',
        loop=loop
    )
    with (await __pool) as conn:
        cur = await conn.cursor()
        await cur.execute("SELECT password('abc')")
        # print(cur.description)
        (r,) = await cur.fetchone()
        assert r == '*0D3CED9BEC10A777AEC23CCC353A8C08A633045E'
        print('ok')
        __pool.close()
        await __pool.wait_closed()

loop.run_until_complete(go())