#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,request,render_template
import asyncio
import threading
import time
# from aiohttp import web

# 二十三、Web开发
# 1.HTTP、HTML、CSS、Javascript
# 2.WSGI：Web Server Gateway Interface，只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：
# application()函数必须由WSGI服务器来调用，如Python内置的一个WSGI服务器叫wsgiref
def application(environ,start_response):    # environ:一个包含所有HTTP请求信息的dict对象
    start_response('200 OK',[('Content-Type','text/html')])     # 发送HTTP响应的函数
    # 两个参数：一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'World')    # 从environ里读取PATH_INFO
    return [body.encode('utf-8')]     # 函数的返回值作为HTTP响应的Body发送给浏览器

# 详见test_8_server.py调用application()


# 3.使用Web框架：处理url到函数的映射，提供了一套开发和部署网站的方式，主要用于动态网络开发，减少不必要的工作量
# 常见的：Django（重量级），Flask（轻量级,anaconda包含）
# Flask自带的Server在端口5000上监听:
'''
处理3个URL，分别是：

GET /：首页，返回Home；
GET /signin：登录页，显示登录表单；
POST /signin：处理登录表单，显示登录结果。
'''
app = Flask(__name__)

@app.route('/',methods=['Get','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='123123':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

#if __name__ == '__main__':
#    app.run()


# 4.使用模板：
# Flask默认支持的模板是jinja2(anaconda包含)
# 编写模板，写好的模板放到templates文件夹下，和py同级目录
'''
jinja2模板中，用{{ name }}表示一个需要替换的变量，{% ... %}表示指令。如：

{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}

除了Jinja2，常见的模板还有：

Mako：用<% ... %>和${xxx}的一个模板；
Cheetah：也是用<% ... %>和${xxx}的一个模板；
Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
'''

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app1.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app1.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='123123':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

# if __name__ == '__main__':
#    app1.run()


# 二十三、异步IO
'''
当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。
异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：
loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)
'''

# 1.协程：又称微线程，纤程。英文名Coroutine。python内通过generator实现。
'''
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

和多线程比，协程有何优势？
最大的优势是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
第二,就是不需要多线程的锁机制，因为只有一个线程，不存在同时写变量冲突，在协程中控制共享资源不加锁，只需判断状态，所以执行效率比多线程高很多。

多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

“子程序就是协程的一种特例。”
'''
# 改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   # 一旦生产了东西，通过c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# 2.asyncio：异步io，https://docs.python.org/zh-cn/3/library/asyncio.html?highlight=async%20def
# 协程 通过 async/await 语法进行声明
'''
hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值，然后接着执行下一行语句。
'''
@asyncio.coroutine  # 把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。从3.8开始不使用@coroutine，用async def
def hello():
    print('Hello World %s' % threading.current_thread)
    r = yield from asyncio.sleep(1)     # 看成是一个耗时1秒的IO操作,此时主线程去执行EventLoop中其他可以执行的coroutine
    print('Hello end %s' % threading.current_thread)

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 新的async def await用法：
async def test():
    print('Hello test')
    await asyncio.sleep(1)
    print('Thanks')

asyncio.run(test())

# 官方案例
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')     # 等1秒
    await say_after(2, 'world')     # 等2秒

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
# 修改以上示例，并发运行两个 say_after 协程:
async def main1():
    task1 = asyncio.create_task(    # 用来并发运行作为 asyncio 任务 的多个协程
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main1())    # 比上面未修改示例快了1秒

# 3.aiohttp：基于asyncio实现的HTTP框架(conda install -c anaconda aiohttp可安装到anaconda里)
'''
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
'''


# 二十四、MicroPython：Python精简版，为了运行在单片机这样的性能有限的微控制器上，最小体积仅256K，运行时仅需16K内存。可以开发机器人
'''
待定
'''