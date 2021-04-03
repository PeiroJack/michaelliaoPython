#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def name_of_email(addr):
    return [x for x in re.split(r'[\<\>\@]+', addr) if x][0]

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')