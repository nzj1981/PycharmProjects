# !/usr/bin/env python3
# coding=utf-8


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):

        if self.score > 100:
            raise ValueError('"Exceeded maximum 100",This score %d' % self.score)
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        elif self.score >= 0:
            return 'C'
        raise ValueError('Wrong value')

