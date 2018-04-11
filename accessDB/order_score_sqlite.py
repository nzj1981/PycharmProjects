# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: order_score_sqlite.py 
@time: 2018/4/11 11:07
"""
import os
import sqlite3

"""
在sqlite中根据分数段查找指定名字
"""

# 创建sqlite数据库
db_file = os.path.join(os.path.dirname(__file__), 'test.db')

if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)

# 初始化数据
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) PRIMARY KEY, NAME VARCHAR(20), score int)')
cursor.execute(r"insert into user values('A001', 'Adam', 95)")
cursor.execute(r"insert into user values('A002', 'Bart', 62)")
cursor.execute(r"insert into user values('A003', 'Lisa', 78)")

# 关闭数据库
def close_db(cursor, conn):
    cursor.close()
    conn.commit()
    conn.close()

close_db(cursor, conn)

# 返回指定分数区间的名字,按分数从低到高排序
def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        names = []
        sql = r"select name from user WHERE score >=? AND score <=? order by score"
        cursor.execute(sql, (low, high))
        for n in cursor.fetchall():
            names.append(n[0])

    finally:
        close_db(cursor, conn)
    return names

# 测试验证
# print(get_score_in(80, 95))
assert get_score_in(80, 95) == ['Adam']
assert get_score_in(60, 80) == ['Bart', 'Lisa']
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam']

print('Success')

