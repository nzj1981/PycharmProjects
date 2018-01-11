# !/usr/bin/env python3
# coding = utf-8

'''
@property的实现比较复杂的。把一个getter方法变成属性，只需要加上@property就可以了
@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
example:
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, v):
        self._width = v

    @height.setter
    def height(self, v):
        self._height = v

    @property
    def resolution(self):
        return self._width * self._height


# 测试

s = Screen()
s.width = 1024
s.height = 768
print('resolution = ', s.resolution)
if s.resolution == 786432:
    print('测试通过')
else:
    print('测试失败')
