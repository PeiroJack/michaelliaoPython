#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入socket库:
import socket
'''
# 创建一个socket：
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接：
# 参数是一个tuple，包含地址和端口号
s.connect(('www.sina.com.cn', 80))
# 80端口是Web服务的标准端口
# SMTP服务是25端口，FTP服务是21端口
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
'''

# 访问https
# ssl
import ssl
s = ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn', 443))

# 发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接受数据：
buffer = []
while True:
    # 每次最多接受1k字节：
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()

# 接收到的数据包括HTTP头和网页本身，
# 我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open(r'17.Socket\sina.html', 'wb') as f:
    f.write(html)

# 把header写入文件:
with open(r'17.Socket\header.txt', 'wb') as f:
    f.write(header)