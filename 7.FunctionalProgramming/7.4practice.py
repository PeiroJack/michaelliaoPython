# -*- coding: utf-8 -*-
__author__ = 'HuangPeirong'

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools


def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		s_time = time.time()
		ff = fn(*args, **kw)
		e_time = time.time()
		print('%s executed in %s ms' % (fn.__name__, e_time - s_time))
		return ff

	return wrapper


# def metric(fn):
# 	@functools.wraps(fn)
# 	def wrapper(*args, **kw):
# 		s_time = time.time()
# 		ff = fn(*args, **kw)
# 		e_time = time.time()
# 		print('%s executed in %s ms' % (fn.__name__, e_time - s_time))
# 		return ff
#
# 	return wrapper

# 测试
@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y


@metric
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z


print(fast.__name__)
print(slow.__name__)

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
	print('测试失败!')
elif s != 7986:
	print('测试失败!')


def log(msg):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if callable(msg):
				print('call %s()' % func.__name__)
			else:
				print('%s %s():' % (msg, func.__name__))
			return func(*args, **kw)

		return wrapper

	if callable(msg):
		return decorator(msg)
	return decorator


# def log(msg):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			if callable(msg):
# 				print('call %s():' % func.__name__)
# 			else:
# 				print('%s %s():' % (msg, func.__name__))
# 			return func(*args, **kw)
#
# 		return wrapper
#
# 	if callable(msg):
# 		return decorator(msg)
# 	return decorator


@log
def now1():
	print('2021-04-03')


@log('execute')
def now2():
	print('2021-04-03')


now1()
now2()

# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
#
# 	return wrapper
#
#
# @log
# def now():
# 	print('2021-04-03')
#
#
# f = now
# f()
# print(now.__name__)

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s:' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# now()
# print(now.__name__)
