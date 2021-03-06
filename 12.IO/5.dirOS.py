#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#利用os模块编写一个能实现dir -l输出的程序。
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
'''

from datetime import datetime
import os

pwd = os.path.abspath('.')
print('      Size  Last Modified    Name')
print('--------------------------------------------------------')

for f in os.listdir(pwd):
    size = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%m')
    flag = '/' if os.path.isdir(f) else ''
    print('%10s  %s  %s%s' % (size, mtime, f, flag))