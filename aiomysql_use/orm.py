# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: orm.py 
@time: 18-4-24 下午6:05
"""
__author__ = 'autumner'

import asyncio
import aiomysql

db = {
    'host': '103.231.145.114',
    'port': 8094,
    'user': 'pyuser',
    'password': 'pyuser123',
    'db': 'awesome'
}

loop = asyncio.get_event_loop()

async def test_example():
    conn = await aiomysql.connect(host='103.231.145.114', port=8094, user='pyuser', password='pyuser123', db='awesome', loop=loop)
    cur = await conn.cursor()
    await cur.execute("select password('abc')")
    print(cur.description)
    (r,) = await cur.fetchone()
    assert r == '*0D3CED9BEC10A777AEC23CCC353A8C08A633045E'
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())