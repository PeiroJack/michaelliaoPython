#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# （通常用16进制的字符串表示）。

# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
# 计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，
# 通常用一个32位的16进制字符串表示。

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。


# 摘要算法能应用到什么地方？举个常用例子：
#任何允许用户登录的网站都会存储用户登录的用户名和口令。
# 如何存储用户名和口令呢？方法是存到数据库表中：
'''
name	password
michael	123456
bob	abc999
alice	alice2008
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。
此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
'''

# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
'''
username	password
michael	e10adc3949ba59abbe56e057f20f883e
bob	878ef96e86145580c38c87f0410ad153
alice	99b1c2188db85afee403b1536010c2c9
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，
如果一致，说明口令输入正确，如果不一致，口令肯定错误。
'''

# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    for key, value in db.items():
        if key == user and value == calc_md5(password):
            return True
    return False
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')