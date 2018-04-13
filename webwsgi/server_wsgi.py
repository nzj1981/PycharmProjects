# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: server_wsgi.py
@time: 2018/4/13 11:05
"""

"""
创建wsgi服务器
"""

# 从wsgiref模块导入
from wsgiref.simple_server import make_server

# 导入我们定义的application函数
from hello_api import application

# 创建一个服务器，IP地址为空，端口是8000 处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求
httpd.serve_forever()
