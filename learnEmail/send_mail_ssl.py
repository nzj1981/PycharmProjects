# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: send_mail.py 
@time: 2018/4/8 15:31
"""
from email.mime.multipart import MIMEMultipart

'''
利用python的email组件SMTP发送邮件
'''

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


'''
From:93628876@qq.com
Password:pw
To:18322313385@163.com
smtp server:smtp.qq.com
加密SMTP
'''

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
# 邮件正文内容同时支持HTML和Plain格式
# 利用MIMEMultipart组合一个HMTL和Plain,要注意指定subtype是alternative
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('轻雪飘扬 <%s>' % from_addr)
msg['To'] = _format_addr('网易用户 <%s>' % to_addr)
msg['Subject'] = Header('加密SMTP方式', 'utf-8').encode()
msg.attach(MIMEText('纯文本内容', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>html格式邮件正文</h1></body></html>', 'html', 'utf-8'))

# SMTP服务执行,加密SMTP两种格式;
# 加密SMTP方式一
server = smtplib.SMTP_SSL(smtp_server, 465)
# 加密SMTP方式二不可用，不知什么原因
# server = smtplib.SMTP(smtp_server, 465)
# server.starttls()

# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)

server.login(from_addr, password)

# 邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()
