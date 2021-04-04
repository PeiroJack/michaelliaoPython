# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    # 返回用户看到的字符串
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 回程序开发者看到的字符串，为调试服务的
    __repr__ = __str__

s = Student('Michael')
print(s)