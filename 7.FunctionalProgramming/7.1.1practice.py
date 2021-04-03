# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'


# 利用`map()`函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：`['adam', 'LISA', 'barT']`，输出：`['Adam', 'Lisa', 'Bart']`：

def normalize(name):
	return name.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的`sum()`函数可以接受一个list并求和，请编写一个`prod()`函数，可以接受一个list并利用`reduce()`求积:

from functools import reduce


def prod(L):
	return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
	print('测试成功!')
else:
	print('测试失败!')


# 利用`map`和`reduce`编写一个`str2float`函数，把字符串`'123.456'`转换成浮点数`123.456`：
def str2float(s):
	return reduce(lambda a, b: a * 10 + b, [t for t in map(
		lambda x: {'.': '.', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x],s) if
											t != '.']) / 10 ** (len((s + '.').split('.')[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
	print('测试成功!')
else:
	print('测试失败!')


