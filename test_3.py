#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
import socket
import threading
import time


# 二十、网络编程：客户端编程、服务器编程
# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
# 1.客户端编程
# TCP：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建一个socket，AF_INET指IPv4，AF_INET6指IPv6，SOCK_STREAM指定使用面向流的TCP协议
s=ssl.wrap_socket(socket.socket())      # https访问要用这条，用上面会提示400错误状态码
s.connect(('www.sina.com.cn', 443))  # 建立连接，参数是一个tuple，包含地址和端口号
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') # 发送数据
# 接收数据
buffer = []
while True:
    d = s.recv(65536)    # 每次最多接收1k字节
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()   # 关闭连接
header,html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

# 2.服务器编程
# 首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理
# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)     #等待连接接入最多5个
print('Waiting for connection...')

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

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# UDP：
'''
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     # SOCK_DGRAM即表示使用UDP协议
s.bind('127.0.0.1',9999)    # 绑定地址和端口，不需要监听
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)       # recvfrom()返回数据和客户端的地址与端口
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)    # sendto()服务器直接将数据返回给客户端

# 客户端：
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))     # 不需要connect()，直接sendto
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))     # 接收数据recv()
s.close()
'''