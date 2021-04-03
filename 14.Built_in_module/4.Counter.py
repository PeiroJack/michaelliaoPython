#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
c.update('hello')
print(c)