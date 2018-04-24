#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: parseJson.py 
@time: 2018/3/17 16:16
"""

'''
利用urllib读取JSON，然后将JSON解析为Python对象
'''

import json
from urllib import request

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    return json.loads(data)

if __name__ == '__main__':
    url=r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
    data = fetch_data(url)
    print(data)
    assert data['query']['results']['channel']['location']['city'] == 'Beijing'
    print('ok')