#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: html_parser.py 
@time: 2018/3/26 11:28
"""

'''
解析https://www.python.org/events/python-events/,输出
Python官网发布的会议时间、名称和地点
'''

from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):

    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # Finding label event elements
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1

        # 处理标签事件名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        # 处理时间为time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        # 处理地址为span元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    def handle_data(self, data):

        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data: data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data

            self.is_get_data = None


parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)

for item in MyHTMLParser.res:
    print('--------------------------------------------------------------')
    for k, v in item.items():
        print('{}:{}'.format(k, v))
