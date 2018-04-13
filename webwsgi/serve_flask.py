# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: serve_flask.py 
@time: 2018/4/13 13:24
"""

"""
flask框架学习
"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p>用户名：<input name="username"></p>
    <p>密  码：<input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''.encode('utf-8')


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
