#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from test_8 import application
from wsgiref.simple_server import make_server


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 运行后通过http://localhost:8000/Herry (或其他名字)即可访问，控制台会打印日志