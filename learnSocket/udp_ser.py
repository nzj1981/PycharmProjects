# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: udp_ser.py 
@time: 2018/4/8 14:53
"""

'''
UDP则是面向无法连接的协议，
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口，就可以直接发数据包。但是能不能到达就不知道了。
UDP优点：
速度快
使用场景：
对于不要求可靠到达的数据，可以使用UDP协议
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9998))

print('Bind UDP on 9998...')

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    print(reply)
    s.sendto(reply.encode('utf-8'), addr)

