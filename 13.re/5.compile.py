#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 编译：
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())

print(re_telephone.match('010-8979').groups())

