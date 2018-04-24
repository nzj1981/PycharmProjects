# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git
@software: PyCharm 
@file: access_orm.py 
@time: 2018/4/11 15:47
"""
"""
通过ORM访问数据库中表数据
"""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

# 创建对象的基类
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

# 创建session
session = DBSession()

# 创建Query查询,filter是where条件,最后调用one()返回唯一行,如果调用all()则返回所有行
# user = session.query(User).filter(User.id=='5').one()
user = session.query(User).all()
# 输出类型和对象的name属性
print('type:', type(user))


# 类对象序列化
def user2dict(u):
    return {
        'id': u.id,
        'name': u.name,
        'addr': u.addr

    }


# ensure_ascii=False解决utf-8编码转换问题
for u in user:
    cls_str = json.dumps(u, default=user2dict, ensure_ascii=False)
    print(cls_str)

# 关闭session
session.close()
