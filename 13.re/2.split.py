#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
r = re.split(r'\s+', 'a b   c')
print(r)

r = re.split(r'[\s\,]+', 'a,b, c  d')
print(r)

r = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(r)