#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: passwdHmac.py 
@time: 2018/3/14 22:54
"""
'''
设计一个验证用户登录的函数，根据用户输入的口令是正确，返回True或False
'''

import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # self.key = username.join(password)
        self.password = hmac_md5(self.key, password)


db = {}


def login(username, password):
    user = db[username]
    print(user.password, "\n", hmac_md5(user.key, password))
    return user.password == hmac_md5(user.key, password)


if __name__ == '__main__':
    db.setdefault('bob', User('bob', 'abc999'))
    db.setdefault('Tom', User('Tom', 'abc999'))
    print(login('bob', 'abc999'))
    print(login('Tom', 'abc999'))
