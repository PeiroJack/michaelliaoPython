# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 999
# AttributeError

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999