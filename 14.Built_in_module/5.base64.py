#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的base64可以直接进行base64的编解码

import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
'''
#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'
'''
# 请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    return base64.b64decode(s+'='*(len(s) % 4))
# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')