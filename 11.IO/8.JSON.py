#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
d = dict(name = 'Bob', age = 20, score=88)
print(json.dumps(d))
str = json.dumps(d)
print(json.loads(str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
s = Student('Bob', 20, 88)
# TypeError: Object of type Student is not JSON serializable
# print(json.dumps(s))

def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj:obj.__dict__))

str = json.dumps(s, default=lambda obj:obj.__dict__)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(str, object_hook=dict2student))