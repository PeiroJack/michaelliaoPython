#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
def is_valid_email(addr):
    if re.match(r'^\w+([+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',addr):
        return True
    return False
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')