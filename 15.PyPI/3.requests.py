#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
'''
url = 'https://www.douban.com/' # 豆瓣首页
r = requests.get(url, headers=headers) 
#print(r.status_code)
#print(r.text)


r = requests.get(url+'search', params={'q': 'python', 'cat': '1001'}, headers= headers)
print(r.url)
print(r.encoding)
print(r.content)
'''

'''
# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json', headers=headers)
print(r.json())
'''

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
'''
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
'''
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
'''
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
'''
# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
'''
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
'''
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# 除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
'''
print(r.headers)
print(r.headers['Content-Type'])
'''

'''
# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
r.cookies['ts']
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
# 要指定超时，传入以秒为单位的timeout参数：
r = requests.get(url, timeout=2.5) # 2.5秒后超时
'''