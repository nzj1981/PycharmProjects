# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/PycharmProjects.git 
@software: PyCharm 
@file: do_collections.py
@time: 2018/5/22 10:19
"""


'''
1.保留最后N个元素
利用collections.deque保留有限历史记录
'''


from collections import deque


def search(lines, pattern, history=5):
    previouse_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previouse_lines
        previouse_lines.append(line)


if __name__ == '__main__':
    with open(r'deque_text.txt') as f:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline, end='')
                print(line, end='')
                print('-' * 20)


'''
2.找出一个序列中出现次数最多的元素
1.统计单词出现频率的collections.Counter方法
2.输出出现频率最高前3的most_common方法
3.手动增加统计次数update
4.利用Counter进行数学计算(+ -)。
'''
words = [
    'look', 'into', 'my', 'if', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don`t", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print('统计单词出现频率:%s' % word_counts)
top_three = word_counts.most_common(3)
print('输出出现频率最高前3单词：%s' % top_three)

# 手动增加统计次数
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
words_counts = Counter(morewords)
words_counts.update(morewords)
print('通过update手动增加单词统计次数：%s' % words_counts['eyes'])
for word in morewords:
    words_counts[word] += 1
print('通过手动增加单词统计次数：%s' % words_counts['eyes'])


print('通过Counter进行数学计算(+ -)\n')
a = Counter(words)
b = Counter(morewords)
print('a: %s,\n b: %s,\n a + b = %s \n' % (a, b, a + b))
print('a: %s,\n b: %s,\n a - b = %s \n' % (a, b, a - b))



with open('deque_text.txt') as f:
    word_cn = Counter(f)
    print('统计出文件deque_text.txt中所有单词出现次数：%s' % word_cn)
    print('统计出文件deque_text.txt中单词出现次数前3的：%s' % word_cn.most_common(3))


'''
3.命名元组nametuple
3.1._replace
'''
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-09-10')
print('sub.length %s' % len(sub))
addr, joined = sub
print('addr=%s, joined=%s' % (addr, joined))
print('addr replace other "addr=%s"' % sub._replace(addr='tomes@example.com').addr)
print('dict to named tuple==============')
Stock =namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
d = dict_to_stock(a)
print('dict to stock: ', d)


'''
4.合并字典
'''
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print('c = (a, b) ChinaMap:', c['x'], c['z'])