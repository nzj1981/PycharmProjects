# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: use_tcp_cli.py 
@time: 2018/3/30 10:32
"""

'''
建立socket的tcp连接的客户端程序 
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 6553))

# 接收欢迎信息
print(s.recv(1024).decode('utf-8'))

for data in [b'Tom', b'Jack', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()