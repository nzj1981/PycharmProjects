# !/usr/bin/env python3
# encoding: utf-8

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site:  https://github.com/nzj1981/PycharmProjects.git
@software: PyCharm 
@file: passwdMd5.py 
@time: 2018/3/14 13:42
"""
import hashlib
import random


# get md5

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# print(get_md5('123.com'))

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)

# print(login('bob', 'abc999'))
