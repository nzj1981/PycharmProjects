# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: read_sqlite.py 
@time: 2018/4/10 17:43
"""

"""
读取sqlite中数据
使用cursor对象执行select语句时,通过featchall()可以拿到结果集
结果集是一个list,每个元素都是一个tuple,对应一行记录
"""

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句
sql = r'select * from USER WHERE id=?'
cursor.execute(sql, ('1',))

# 得到查询结果集
values = cursor.fetchall()

# 输出结果集
print(values)

# 关闭连接
cursor.close()
conn.close()
