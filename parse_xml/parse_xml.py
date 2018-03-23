#!/usr/bin/env python3
# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: parse_xml.py 
@time: 2018/3/21 13:17
"""
'''
Get the weather forecast for Beijing in the past 5 days
'''

from xml.parsers.expat import ParserCreate
from urllib import request
from datetime import datetime


def parseXml(xml_str):
    data = {'city': '', 'forecast': []}

    def start_element(name, attrs):
        # print(name)
        if name == 'yweather:location' and 'city' in attrs:
            data['city'] = attrs['city']
        elif name == 'yweather:forecast' and 'date' in attrs and 'high' in attrs and 'low' in attrs:
            data['forecast'].append(
                {'date': datetime.strptime(attrs['date'], '%d %b %Y').strftime('%Y-%m-%d'),
                 'high': round((int(attrs['high']) - 32) / 1.8),
                 'low': round((int(attrs['low']) - 32) / 1.8)})

    parser = ParserCreate()
    parser.StartElementHandler = start_element
    parser.Parse(xml_str)
    return data


url = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(url, timeout=10) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))

print(result)
