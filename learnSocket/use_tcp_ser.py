# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: use_tcp_ser.py 
@time: 2018/3/30 10:07
"""
import threading

import time

'''
socket 用法
先建立服务端
'''

import socket
import threading

# 创建一个基于IPV4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听端口
s.bind(('127.0.0.1', 6553))

# 调用listen()方法开始监听,传入参数指定等待连接的最大数量
s.listen(10)
print('Waiting for connection...')


# 创建线程或进程方法
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 建立服务永久在线
while True:
    # 接受一个新连接,accept()会等待并返回现代战争客户端边接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


