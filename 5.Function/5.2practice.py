# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

import math

def quadratic(a, b, c):
	if not (isinstance(a, (int, float)) | isinstance(b, (int, float)) | isinstance(c, (int, float))):
		raise TypeError('bad operand type')
	temp = math.sqrt(b ** 2 - 4 * a * c)
	if temp == 0:
		return -b / (2 * a)
	else:
		return (-b + temp) / (2 * a), (-b - temp) / (2 * a)


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')