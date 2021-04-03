#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.name)
#os.uname()
#print(os.environ.get('PATH'))
#print(os.environ.get('x', 'default'))
#print(os.path.abspath('.'))
path = os.path.join(r'C:\Users\peiroJack\Desktop\python\11.IO','testdir')
path2 = os.path.join('.','testdir')
print(path)
#os.mkdir(path)
#os.rmdir(path)

print(os.path.split(r'C:\Users\peiroJack\Desktop\python\11.IO\4.OS.py'))
print(os.path.splitext(r'C:\Users\peiroJack\Desktop\python\11.IO\4.OS.py'))

# 对文件重命名:
#s.rename('test.txt', 'test.py')
# 删掉文件:
#os.remove('test.py')

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])