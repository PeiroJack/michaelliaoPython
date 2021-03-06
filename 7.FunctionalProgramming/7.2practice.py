# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'


def countno():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i

		fs.append(f)
	return fs


f1, f2, f3 = countno()

print(f1())
print(f2())
print(f3())


def count():
	def f(j):
		def g():
			return j * j

		return g

	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
	def g():
		n = 0
		while True:
			n += 1
			yield n

	a = g()

	def counter():
		return next(a)

	return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
	print('测试通过!')
else:
	print('测试失败!')

# def createCounter():
# 	x = 0
#
# 	def counter():
# 		nonlocal x
# 		x = x + 1
# 		return x
#
# 	return counter

##################################

# def createCounter():
# 	L = [0]
#
# 	def counter():
# 		L[0] += 1
# 		return L[0]
#
# 	return counter

##################################

# def createCounter():
# 	def g():
# 		n = 0
# 		while True:
# 			n += 1
# 			yield n
#
# 	a = g()
#
# 	def counter():
# 		return next(a)
#
# 	return counter
