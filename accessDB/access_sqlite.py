# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: access_sqlite.py 
@time: 2018/4/10 16:49
"""
'''
访问sqlite数据库
使用cursor对象执行insert, update, delete语句时,执行结果由
rowcount返回影响的行数,就可以拿到执行结果.
'''

# 导入SQLite驱动
import sqlite3
import os

"""
连接到SQLite数据库
数据库文件是test.db
如果文件不存在,会自动在当前目录创建
"""
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)

# 创建一个Cursor:
cursor = conn.cursor()

# 创建user表
sql = 'create table user(id varchar(20) primary key, name VARCHAR(20))'
cursor.execute(sql)

# 插入一条记录
sql1 = r"insert into user(id, name) values('1', 'Michael')"
cursor.execute(sql1)

# 通过rowcount获得插入行数
print(cursor.rowcount)

# 关闭cursor
cursor.close()

# 提交事务
conn.commit()

# 关闭connection
conn.close()