# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: access_mysql.py 
@time: 2018/4/11 13:43
"""

# 导入MySQL驱动
import mysql.connector

"""
关闭数据库连接
"""
def close_db(cursor, conn):
    cursor.close()
    conn.commit()
    # conn.close()
    return True

"""
连接mysql数据库
CREATE DATABASE `py_test` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
insert into mysql.user(Host,User,Password,ssl_cipher,x509_issuer,x509_subject) values("%","pyuser",password("pyuser123"),"","","");
Grant all privileges on py_test.* to 'pyuser'@'%' identified by 'pyuser123' with grant option;
flush privileges;
"""

conn = mysql.connector.connect(user='pyuser', password='pyuser123', host='ip', port='3306', database='py_test')

cursor = conn.cursor()

# 创建user表
cursor.execute(r"drop table if EXISTS `user`")
cursor.execute(r"create table user(id varchar(20) PRIMARY key, NAME VARCHAR(20))")

# 插入一条记录
cursor.execute(r"insert into user(id, NAME ) values(%s, %s)", ('1', '中国人'))
cursor.execute(r"insert into user(id, NAME ) values(%s, %s)", ['2', 'Tom'])
cursor.execute(r"insert into user(id, NAME ) values(%s, %s)", ['3', '高尚人'])

# 插入成功返回1,输出ok
if cursor.rowcount:
    print('ok')

# 关闭数据库
close_db(cursor, conn)

# 查询mysql的user表数据
try:
    cursor = conn.cursor()
    # cursor.execute(r"select * from user where id = %s", ('1',))
    cursor.execute(r"select * from user")
    values = cursor.fetchall()
    print(values)
finally:
    close_db(cursor, conn)
    conn.close()