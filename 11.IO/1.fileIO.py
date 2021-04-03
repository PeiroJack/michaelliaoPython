#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fpath = r'C:\Users\peiroJack\Desktop\python\11.IO\timezone.txt'
with open(fpath, 'r') as f:
    str = f.read()
    print(str)

with open(fpath, 'w') as f:
    f.write('Hello, Write')