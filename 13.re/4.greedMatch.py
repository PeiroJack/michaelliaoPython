#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
# 贪婪匹配（默认）
print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 非贪婪匹配 加 ？
print(re.match(r'^(\d+?)(0*)$', '102300').groups())