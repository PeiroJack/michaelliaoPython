#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
m = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(m)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

