# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: udp_cli.py 
@time: 2018/4/8 15:02
"""


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michal', b'Tracy', b'Sarah']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9998))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()