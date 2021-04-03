# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'
# 获得当前目录下所有文件和目录名
import os
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
	print('测试通过!')
else:
	print('测试失败!')


