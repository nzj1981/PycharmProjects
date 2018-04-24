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
注意：使用163邮件箱做发邮件者会报554错误，
原因如下：
•554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；

•554 DT:SUM 信封发件人和信头发件人不匹配；

•554 IP is rejected, smtp auth error limit exceed 该IP验证失败次数过多，被临时禁止连接。请检查验证信息设置；

•554 HL:IHU 发信IP因发送垃圾邮件或存在异常的连接行为，被暂时挂起。请检测发信IP在历史上的发信情况和发信程序是否存在异常；

•554 HL:IPB 该IP不在网易允许的发送地址列表里；

•554 MI:STC 发件人当天内累计邮件数量超过限制，当天不再接受该发件人的投信。请降低发信频率；

•554 MI:SPB 此用户不在网易允许的发信用户列表里；

•554 IP in blacklist 该IP不在网易允许的发送地址列表里。
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
msg['Subject'] = Header('邮件正文支持两种格式', 'utf-8').encode()
msg.attach(MIMEText('纯文本内容', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>html格式邮件正文</h1></body></html>', 'html', 'utf-8'))

# SMTP服务执行
server = smtplib.SMTP(smtp_server, 25)

# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)

server.login(from_addr, password)

# 邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()
