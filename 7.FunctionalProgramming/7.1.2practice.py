# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'


def is_odd(n):
	return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
	return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))



def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n


def _not_divisible(n):
	return lambda x: x % n > 0


def primes():
	yield 2
	it = _odd_iter()  # 初始序列
	while True:
		n = next(it)  # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it)  # 构造新序列


#  打印1000以内的素数:
for n in primes():
	if n < 1000:
		print(n)
	else:
		break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	return str(n)[::] == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
												  111, 121, 131, 141, 151, 161, 171, 181, 191]:
	print('测试成功!')
else:
	print('测试失败!')
