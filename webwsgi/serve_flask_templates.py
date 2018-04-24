# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: serve_flask_templates.py 
@time: 2018/4/13 13:49
"""

"""
flask的template学习
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    page_list = [1, 2, 3, 4, 5]
    welcome_str = "欢迎使用flask框架！"
    return render_template('home.html', **locals())


@app.route('/signin', methods=['GET'])
def signin_form():
    form_str = "请填写以下表单："
    return render_template('form.html', **locals())


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return render_template('sigin-ok.html', username=username)

    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()
