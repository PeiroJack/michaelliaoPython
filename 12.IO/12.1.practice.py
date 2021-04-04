# -*- coding: utf-8 -*-

from os import path

print(path.dirname(__file__)) #获取当前路径
fpath = path.dirname(__file__)+r'/timezone.txt'

with open(fpath, 'r') as f:
    str = f.read()
    print(str)

with open(fpath, 'w') as f:
    f.write('Hello, Write')