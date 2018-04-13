# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: hello_api.py 
@time: 2018/4/13 11:04
"""
"""
wsgi接口定义
"""

def application(environ, start_respones):
    start_respones('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, web!</h1>']

    # 增加body
    body = 'Hello, %s!' % (environ['PATH_INFO'][1:] or 'welcome')
    return [body.encode('utf-8')]