#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time


# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，
# 也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。
# 127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，
# 客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。

# 我们要绑定监听的地址和端口
s.bind(('127.0.0.1',9999))

# listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。
# 如果客户端发送了exit字符串，就直接关闭连接。
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


#服务器程序通过一个永久循环来接受来自客户端的连接，
#accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

