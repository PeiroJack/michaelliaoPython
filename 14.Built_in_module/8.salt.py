#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，
如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。

考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，
黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：
'e10adc3949ba59abbe56e057f20f883e': '123456'
'21218cca77804d2ba1922c33e0151105': '888888'
'5f4dcc3b5aa765d61d8327deb882cf99': 'password'
这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？

由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
def calc_md5(password):
    return get_md5(password + 'the-Salt')
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，
这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？
如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，
从而实现相同口令的用户也存储不同的MD5。
'''

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
# 然后，根据修改后的MD5算法实现用户登录的验证：
# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    password = password + user.salt
    return user.password == get_md5(password)
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')