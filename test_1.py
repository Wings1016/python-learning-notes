#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import chardet
import psutil
import requests

' a learning note'

__author__ = 'Hello'

# 导入socket库
from PIL import ImageFilter, ImageDraw, ImageFont
from tkinter import *
from future.moves.tkinter import messagebox
import PIL
from turtle import *


# 十七、常用第三方模块

# 1.Pillow:图像处理库
# 打开一个jpg图像文件，注意是当前路径:
im = PIL.Image.open('test.jpg')     # tkinter中也含有Image类，要区分，否则会报错
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

# ImageDraw绘图 如要生成字母验证码图片:
# 随机字母:


def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:


def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# 随机颜色2:


def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 240 x 60:
width = 60 * 4
height = 60
image = PIL.Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 20, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# 2.requests：处理URL资源特别方便（比urllib）
r1 = requests.get('https://www.google.com/')
print(r1.status_code)       # 获取headers
with open('/Users/herry/Documents/python/test1.txt', 'w') as file9:
    file9.write(r1.text)     # r.text即get到的页面内容

r2 = requests.get('https://www.douban.com/search',
                  params={'q': 'python', 'cat': '1001'})
print(r2.url)     # 实际请求的URL:https://www.douban.com/search?q=python&cat=1001
# requests自动检测编码，可以使用encoding属性查看：
print(r2.encoding)
# print(r2.content)     # 用content属性获得bytes对象
# 对于特定类型的响应，例如JSON，可以直接获取(这里url失效)
# r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r3.json())
# 通过dict传入headers
r1 = requests.get('https://www.douban.com/', headers={
                 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# 发送post请求
r2 = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r3 = requests.post('https://www.google.com', json=params)  # 内部自动序列化为JSON

# 同样，上传文件需要更复杂的编码格式，requests把它简化成files参数：
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post('https://www.google.com', files=upload_files)

# 获取headers、cookies，提交cookie，设置超时：
# r.headers,r.cookies[''],r = requests.get(url, cookies=cs)
# r = requests.get(url, timeout=2.5) # 2.5秒后超时

# 3.chardet:检测未知编码，支持多种语言
print(chardet.detect(b'Hello, world!'))     # confidence字段，表示检测的概率是1.0（即100%）
data1 = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data1))

# 4.psutil：process and system utilities 实现系统监控
print(psutil.cpu_count())  # 获取CPU逻辑数量
print(psutil.cpu_count(logical=False))  # 获取CPU物理核心数
print(psutil.cpu_times())   # 获取CPU用户/系统/空闲时间
# 类似top命令查询cpu使用率
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
# 获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 获取磁盘信息
# 磁盘分区信息，文件格式是APFS，opts中包含rw表示可读写，journaled表示支持日志
print(psutil.disk_partitions(), '\n')
print(psutil.disk_usage('/'), '\n')  # 磁盘使用情况
print(psutil.disk_io_counters(), '\n')  # 磁盘IO
# 获取网络信息
print(psutil.net_io_counters(), '\n')  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs(), '\n')  # 获取网络接口信息
print(psutil.net_if_stats(), '\n')  # 获取网络接口状态
# 获取当前网络连接信息，要走系统接口，需要root权限,sudo运行
# print(psutil.net_connections())
# 获取进程信息
print(psutil.pids(), '\n')  # 所有进程ID
'''
p1 = psutil.Process(3553)
print(p1.name(),p1.cwd(),p1.cmdline())    # 进程名称,进程工作目录，进程启动的命令行
>>> p.ppid() # 父进程ID
3765
>>> p.parent() # 父进程
<psutil.Process(pid=3765, name='bash') at 4503144040>
>>> p.children() # 子进程列表
[]
>>> p.status() # 进程状态
'running'
>>> p.username() # 进程用户名
'michael'
>>> p.create_time() # 进程创建时间
1511052731.120333
>>> p.terminal() # 进程终端
'/dev/ttys002'
>>> p.cpu_times() # 进程使用的CPU时间
pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
>>> p.memory_info() # 进程使用的内存
pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
>>> p.open_files() # 进程打开的文件
[]
>>> p.connections() # 进程相关网络连接
[]
>>> p.num_threads() # 进程的线程数量
1
>>> p.threads() # 所有线程信息
[pthread(id=1, user_time=0.090318, system_time=0.062736)]
>>> p.environ() # 进程环境变量
'''
# test()函数，可以模拟出ps命令的效果：
print(psutil.test())

# 十八、virtualenv：用来为一个应用创建一套“隔离”的Python运行环境，让需要不同环境的程序“独立”运行
'''
pip3 install virtualenv # 安装
virtualenv --no-site-packages venv # 创建
# 如果virtualenv版本大于20，加上--no-site-packages时候会报错，默认版本大于20是不用加的
source venv/bin/activate # 进入venv环境
# trustasiadeMacBook-Pro:myproject herry$ source venv/bin/activate
# (venv) trustasiadeMacBook-Pro:myproject herry$ pip install jinja2
deactivate # 退出当前venv环境
'''

# 十九、图形界面
# Python支持多种图形界面的第三方库，包括：Tk、wxWidgets、Qt、GTK，本身自带支持Tk的Tkinter
# Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。所以，我们的代码只需要调用Tkinter提供的接口就可以了。
# 如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

class Application(Frame):   # 从Frame派生一个类，是所有widget的父容器
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')     # 每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
        self.helloLabel.pack()      # pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


class Application1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'      # 让用户自己输入
        messagebox.showinfo('Message', 'Hello, %s' % name)  # 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，使用tkMessageBox.showinfo()可以弹出消息对话框。

app = Application1()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

# 1.海龟绘图：Python内置了turtle库
# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
