#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 爬某链接里的图片

from bs4 import BeautifulSoup
import socket
import ssl

# 建立连接获取html
def gethtml(url):
    s=ssl.wrap_socket(socket.socket())      # https访问要用这条，用上面会提示400错误状态码
    s.connect((url, 443))  # 建立连接，参数是一个tuple，包含地址和端口号
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
    with open('new.html', 'wb') as f:
        f.write(html)

# 处理html
def dealhtml():
    with open('new.html') as html_doc:
        soup = BeautifulSoup(html_doc,'html.parser')
        img = soup.find_all('img')
        result = []
        for i in range(len(img)):
            result.append(img[i].attrs['src'])
        print(result)

if __name__=='__main__':
    url = 'www.sina.com.cn'
    gethtml(url)
    dealhtml()
