# !/usr/bin/env python3
# encoding: utf-8
# set(  = "https://github.com/nzj1981/PycharmProjects.git" )

""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site:  
@software: PyCharm 
@file: toTimestamp.py 
@time: 2018/3/5 13:26
"""

import re
from datetime import datetime, timezone, timedelta

'''
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30, 以及一个时区信息如UTC+5:00,均是str，
请编写一个函数将其转换为timestamp
'''


def to_timestamp(dt_str, tz_str):
    # 将字符串日期转换为datetime
    dt_str = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 正则获取需要加减的时区信息(+7, -9)
    tz_str = re.match(r'UTC([+-]\d+):00', tz_str).group(1)
    # 强制设置为UTC
    dt = dt_str.replace(tzinfo=timezone(timedelta(hours=int(tz_str))))
    return dt.timestamp()


if __name__ == '__main__':
# 测试
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
    assert t2 == 1433121030.0, t2
    print('ok', type(t1), t2)
