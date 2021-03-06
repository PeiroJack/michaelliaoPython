# -*- coding: utf-8 -*-

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list)


class Chain(object):
	def __init__(self, path=''):
		self.__path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self.__path, path))

	def __call__(self, path):
		return Chain('%s/%s' % (self.__path, path))

	def __str__(self):
		return self.__path

	__repr__ = __str__


print(Chain().users('michael').repos)  # /users/michael/repos
print(callable(Chain()))