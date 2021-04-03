#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Get
# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

'''
from urllib import request

from urllib.request import urlopen, Request

url = 'http://www.httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
ret = Request(url, headers=headers)
with request.urlopen(ret) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
'''


'''
如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
'''

'''
from urllib import request

req = request.Request('https://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

#我们模拟一个微博登录，先读取登录的邮箱和口令，
# 然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
'''
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

'''
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
'''

'''
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

# 练习
# 利用urllib读取JSON，然后将JSON解析为Python对象：
'''
from urllib import request
import json

def fetch_data(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        if not f.status == 200: raise ValueError('请求失败')
        data = json.loads(f.read().decode('utf-8'))
        print(data)
        return data

# 测试
URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
assert data['answer'] == 'yes' and data['forced']== False
print('ok')
'''
