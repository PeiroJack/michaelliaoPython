# -*- coding: utf-8 -*-

# class Hello(object):
#    def hello(self, name='world'):
#        print('Hello, %s.' % name)

# from hello import Hello

# 用type创造class

def fn(self, name='world'):
	print('Hello %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello('hpr')
print(type(Hello))
print(type(h))

# def fn(self, name='world'):
#     print('Hello, %s' % name)
#
# Hello = type('Hello',(object,),dict(hello=fn))
#
#
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
