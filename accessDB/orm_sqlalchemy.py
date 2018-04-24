# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: orm_sqlalchemy.py 
@time: 2018/4/11 15:30
"""

"""
使用ORM对象,采用python的SQLAlchemy组件
"""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    addr = Column(String(50))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://pyuser:pyuser123@ip:3306/py_test')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 创建新User对象
new_user = User(id='7', name='中国人', addr='北京市西城区')

# 添加到session
session.add(new_user)

# 提交即保存到数据库
session.commit()

# 关闭session
session.close()

