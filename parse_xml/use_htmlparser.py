#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: use_htmlparser.py 
@time: 2018/3/23 13:49
"""

'''
利用HTMLParser，可把网页中的文本、图像等解析出来
feed()方法可以多次调用,也可以一部分一部分塞进去.
特殊字符有两种,一种是英文表示的&nbsp;, 一种是数字表示的
&#1234;,这两种字符可以通过Parser解析出来.
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>---%s' % (tag, attrs))

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

    def handle_pi(self, data):
        print('div: %s' % data)

parser = MyHTMLParser()

parser.feed('''<html>
<head>title</head>
<body>
<!--test html parser-->
<p> Some <a href=\"#\">html</a> &#9650;&nbsp;HTML&nbsp;&equiv; tutorial...<br/>
<div height=\"12\" width=\"200\"> <h2>codepoint-div</h2> </div>
end</p>
</body></html>''')
