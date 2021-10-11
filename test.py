#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a learning note'

__author__='Hello'

# 导入socket库
import math
from collections.abc import Iterable
from collections.abc import Iterator
from functools import reduce,wraps
import functools
import logging
import hello
import sys
import types
from enum import Enum,unique
import pdb
import doctest
from io import BytesIO, StringIO
import os
import pickle
import json
from multiprocessing import Pool, Process, Queue
import time
import random
import subprocess
import threading
import re
from datetime import datetime, timedelta, timezone
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple
import argparse
import base64
import struct
import hashlib
import hmac
import itertools
from contextlib import closing, contextmanager
from urllib.request import urlopen
from urllib import request,parse
from xml.parsers.expat import ParserCreate
from html.parser import HTMLParser
from html.entities import name2codepoint
import requests
import chardet
import psutil

#一、输出
print('hello, world')
print('The quick brown fox', 'jumps over', 'the lazy dog')

#输入
#name = input('please enter your name: ')   #input返回的是str字符串
#print("Hello",name,"!")

#二、数据类型和变量：整数、浮点数1.8e-2、字符串、布尔值、变量、常量
print('I\'m \"OK\"!')   #\转义
print(r'\\b\\') #r''表示''内部的字符串默认不转义
print('''aaa
bbb
ccc''')  #多行
a = 'ABC'
b = a
a = 'XYZ'
print(b)
PI = 10/3   #通常用全部大写的变量名表示常量
print(10 // 3)  #整除

#字符串编码：Python3中，字符串是以Unicode编码
print(ord('A')) #ord获取字符的整数表示
print(chr(25991))   #chr转换为字符
print('\u4e2d\u6587')   #十六进制表示‘中文’ 
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes,用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x.decode('ascii')) #decode将bytes转为str
print(len('ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'))  #len()计算str字符数，bytes字节数，这里输出3，6
#格式化输出%、format、f-string
print('Hi, %s, you have $%d.' % ('Herry', 1000000))
print('growth rate: %d %%' % 7) #%%转义%
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) #format()依次传入{0}{1}参数
a='Herry'
b=1000000
print(r'测试%传参：','%s,%d' % (a,b))    #%使用变量传参ok
#f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

#三、list、tuple
#1.list:有序列表[]，[0][1][2]，可以随意增删元素insert、append、pop
classmates = ['Michael',123,['Bob','ABC'],5*9]  #可以嵌套list
print(classmates[-1])   #-1是直接取最后一个元素，以此类推-2倒数第二个
classmates.insert(1,'Herry')    #插入指定位置
classmates.append('Adam')   #追加到最后
classmates.pop(0)   #删除指定位置pop(i)
print(classmates)   #输出结果为['Herry', 123, ['Bob', 'ABC'], 45, 'Adam']

#2.tuple:有序元组()，一旦初始化就不能更改，可以为空
friend=('L',)   #只有一个元素要加,
roommates=('Michael',['123',456],'Bob')
roommates[1][0]='789'   #元组roomates[1]指向的list元素可以更改，tuple[1]的指向还是没有更改的
print(roommates)    #输出结果为('Michael', ['789', 456], 'Bob')

#四、条件判断if、elif、else
age = input('Your age:')
age = int(age)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#循环
#1.for  in  依次把list或tuple中的每个元素迭代出来
sum1 = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum1 = sum1 + x
print(sum1)
sum2 = 0
for x in list(range(100)):  #range()生成证书序列，list()再转为list类型
    sum2 = sum2 + x
print(sum2)

# 循环语句支持 else 子句；for 循环中，可迭代对象中的元素全部循环完毕时，或 while 循环的条件为假时，
# 执行该子句；break 语句终止循环时，不执行该子句。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#2.while
#3.break、continue:不要滥用，大多数循环并不需要用到break和continue语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#五、dict和set
#1.dict{} 键值对，类似其他语言的map；key不存在会报错
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Bob')    #删除key和对应的value
#判断是否存在对应的key：1 in 2，get()
print('Thomas' in d)
print(d.get('Thomas'))  #不存在默认是None，若要指定返回值，可d.get('Thomas',-1)
#和list比较，dict有以下几个特点：
'''
查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。
'''

#2.set:一组key集合，不存value，key不重复
se1 = set([1,2,2,2,3,3,4,5,6,5])
se1.add(5)   #add添加，remove删除
se1.remove(1)
print(se1)   ##结果为2，3，4，5，6
se2 = set([1,1,2,2,2,3,3,3,3,9])
print(se1 & se2)    #可以看作两个集合，求交集&、并集｜
print(se1 | se2)


#六、函数
abs(-20)
max(1,2,4)
int('123')
float(123)
#定义函数def
def my_abs(x):
    if not isinstance(x, (int, float)):     #isinstance()内置数据类型检查函数
        raise TypeError('bad operand type')   #自定义函数默认没有参数检查
    if x >= 0:
        return x
    else:
        return x,-x    #可返回多个值，即返回一个tuple
print(my_abs(-99))      #结果为(-99,99)
#空函数：pass可做占位符
def nop():
    pass
#计算n次方
#必选参数在前，默认参数在后。定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):      #默认参数n=2计算平方，则可以通过power(x)就计算出平方，如果计算三次方则power(x,n)
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(6,3))   #216

#可变参数：*，在函数调用时会自动组成tuple
def calc(*numbers):
    sum3 = 0
    for n in numbers:
        sum3 = sum3 + n * n
    return sum3
print(calc(1,3,5,7,9))  #165,如果不使用可变参数，则调用需要calc((1,3,5,7,9))或者calc([1,3,5,7,9])
#调用可变参数
numberrrr=[1,2,3,4,5]
print(calc(*numberrrr))     #55，用*调用list或tuple的所有元素作为可变参数传进去

#关键字参数：可接受任意数量>=0含参数名的参数,使用**,调用时会自动成为一个dict，即键值对
def person(name, age, **kw):        #关键字参数kw
    print('name:', name, 'age:', age, 'other:', kw)
person('Herry','17',sex='Boy',localtion='Shanghai')     #结果为name: Herry age: 17 other: {'sex': 'Boy', 'localtion': 'Shanghai'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)     # **extra自动将所有的键值对传进去

#命名关键字参数：要限制关键字参数的名字；可以有默认值
def person(name, age, *, city='Shanghai', job):        #用*隔开，*后表示只接收city和job作为关键字参数，有可变参数的话就不需要再写*
    print(name, age, city, job)

#参数组合：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#递归参数:定义简单，逻辑清晰
#函数调用是通过栈实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#由于栈的大小不是无限的，所以递归调用的次数过多会导致栈溢出。可以试试fact(1000)
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(3))

#避免栈溢出可以通过尾递归优化。尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#但是Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)    #返回值只掉调用函数本身

#七、高级特性：优化代码，提高效率
#1.切片
classmates[0:2] #取前两个元素，下标从0开始
L = list(range(100))
print(L[:-1])       #去掉最后一个元素
print(L[-10:])     #取后10个数    
print(L[:10:2])   #前10个，每两个取一次
print(L[::5])     #每5个取一次
print(roommates[:3])    #tuple取前三个
print('ABCDEFG'[::2])   #字符串切片，类似substring
print('ABCDEFG'[::-1])  #逆转str

s = '   hello'
def trim(s):
    if len(s)==0:
        return s
    else:
      while s[0]==' ':
        s=s[1:]
      while s[-1]==' ':
        s=s[:-1]
      return s 
print(trim(s))

# 2.迭代
# 默认情况下，dict迭代的是key，顺序可能不一样。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。
d = {'a': 1, 'b': 2, 'c': 3}
for key,values in d.items():
    print(key,values)
# 判断一个对象是否是可迭代对象：可通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))
# Python内置的enumerate函数可以把一个list变成索引-元素对，即对下标循环
for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
def findMinAndMax(L):
    if len(L) == 0:
        return(None,None)
    max=min=L[0]
    for x in L:
       if x > max:
           max = x
       if x < min:
           min = x
    return (min, max)

# 3.列表生成式
list(range(1, 11))
#生成1x1 2x2 3x3  10x10
L = []
for x in range(1, 11):  #循环
    L.append(x * x)
L1 =  [x * x for x in range(1, 11)]    #用列表生成式
print(L1)
L2 = [x * x for x in range(1, 11) if x % 2 == 0]    #加上if筛选偶数
print(L2)
L3 = [m + n for m in 'ABC' for n in 'XYZ']       #两层循环-全排列
print(L3)
L4 = [x if x % 2 == 0 else 0 for x in range(1, 11)]    #for后面的if是过滤条件，不能有else
print(L4)
L11 = ['Hello', 'World', 18, 'Apple', None]
L22 = [x.lower() for x in L11 if isinstance(x,str)]
print(L22)

# 4.生成器：一边循环一边计算的机制generator，可迭代，相比于列表生成式可节省内存空间
g = (x * x for x in range(10))
print(g)    #结果为<generator object <genexpr> at 0x1021e99e0>
print(next(g)) 
print(next(g))      #通过不断调用next(g)打印g的元素，对比for循环而言比较麻烦
print('--------')
for n in g:
    print(n)
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator，斐波那契数列例子如下：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b     # 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
        a, b = b, a + b     # 赋值，相当于t=[b,a+b],a=t[0],b=t[1]
        n = n + 1
    return 'done'
# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        for i in range(len(L)):
            L[i]=L[i-1]+L[i+1]
            pass

# 5.迭代器：可以被next()函数调用并不断返回下一个值，直到没有数据时抛出StopIteration错误的对象称为迭代器：Iterator，
print(isinstance((x for x in range(10)), Iterator))     #生成器都是迭代器的对象
print(isinstance([], Iterator))     
print(isinstance(iter([]), Iterator))   #可以通过iter()将可迭代Iterable的转为迭代器
# Python的for循环本质上就是通过不断调用next()函数实现的
            
# 八、函数式编程：其中一个特点即允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# 1.高阶函数:一个可以接收另一个函数作为参数的函数
f = abs     # 函数名其实就是指向函数的变量
print(f(-99))
def add(x, y, f):   #绝对值求和
    return f(x) + f(y)
print(add(-11,-32,f))   #输出43

# 1.1 map/reduce
# 1.1.1 map()函数接收一个函数和一个Iterable，将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
print(list(map(f,[1,2,3,4,5,6,7,8,9,10])))      #将逐个计算抽象化
print(list(map(str,[1,2,3,4,5])))
# 1.1.2 reduce()把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列中下一个元素做累积计算，比如求和
def f1(x,y):
    return x+y
print(reduce(f1,[1,3,5,7,9]))   #即f1先作用于1，3，然后再作用于4，5，以此类推
# 练习：把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
stringgggg=['adam', 'LISA', 'barT']
def lower(x):
    if ord(x)<97:
       return chr(ord(x)+32)
    else:
        return x
def normalize(name):
    test=list(name)
    if ord(test[0])>96:
       test[0]=chr(ord(test[0])-32)
    test[1:]=list(map(lower,test[1:]))
    return ''.join(test)
resultttt=list(map(normalize,stringgggg))
print(resultttt)
# 字符串转换为浮点数
def str2float(s):
    ss1=s.split('.')[0]
    ss2=s.split('.')[1]
    def before(x,y):
        return x*10+y
    a=reduce(before,list(map(int,ss1)))     #list(str)<==>list(int)通过list(map(int/str,l))实现
    b=reduce(before,list(map(int,ss2)))
    c=b/math.pow(10,len(ss2))       #math.pow(a,b)求a的b次幂
    return a+c
s='123.4567'
ss1=s.split('.')[0]
ss2=s.split('.')[1]
print(str2float(s))

# 1.2 filter():把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素,返回的是一个Iterator
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 素数序列练习
def _odd_iter():    #生成从3开始的奇数序列  
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):      #筛选函数
    return lambda x: x % n > 0
def primes():   #生成素数序列
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印10以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break
# 回数筛选
def is_palindrome(n):
    s=list(n)
    count=0
    while count<len(s):
        if s[count]==s[len(s)-count-1]:
            continue
        else:
            return False
            break
        count=count+1

# 1.3 sorted():根据key指定的函数作用到每一个元素，然后排序
print(sorted([36, 5, -12, 9, -21]))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))   #key指定化为小写字母，然后逆序从大到小排，即Zoo第一个

# 2.返回函数：函数作为返回值
# 闭包：在一个内部函数中，对外部作用域的变量进行引用，(并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包。  闭包可以保存当前的运行环境  
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:      #内部函数sum可以引用外部函数lazy_sum的参数和局部变量args
            ax = ax + n
        return ax
    return sum      #当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closre）”程序结构
print(lazy_sum(1,3,5,7,9))       #<function lazy_sum.<locals>.sum at 0x10b3f2160>
f1 = lazy_sum(1, 3, 5, 7, 9)    #这里f1是lazy_sum返回的函数sum()
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1())     #真正调用sum()运算结果
print(f1==f2)       #False，每次都会返回新的函数
sss=range(1,4)
print(sss)
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())
# 练习，写一个计数器函数，即递增，每次输出加一，每次调用后1，2，3，4，5。。。
# 方法一：利用nonlocal关键字声明变量x，既不是局部变量，也不是全局变量，需要向上一层变量空间找这个变量。只在闭包里面生效，只能用在嵌套函数中，
# 是python3中新添的关键字，python2中无。（作用理解是：x保存内函数counter每次作用后返回的值，
# 比如第一次x=0，counter()后，x=0+1=1，counter（）后，x=1+1=2以此类推）
def createCounter():
    x=0
    def counter():
        nonlocal x
        x=x+1
        return x
    return counter
# 方法二：利用可变数据类型list
def createCounter():
    L=[0]   #初始化列表L为0
    def counter():
        L[0]+=1     #L[0]指的是列表L的第一个元素，为一个可变变量
        return L[0]
    return counter
# 方法三：利用生成器
def createCounter():
    def g():    #生成器生成有序数列1，2，3
        n=0
        while 1:
            n+=1
            yield n
    a=g()
    def counter():
        return next(a)  #每次调用next()函数获得生成器的下一个返回值
    return counter
#方法四：利用len()
def createCounter():
    L=[]
    def counter():
        L.append(9) #这里只是为了补位，添加任何一个数字都可以的
        return len(L)
    return counter

# 3.匿名函数：关键字lambda。lambda x: x * x冒号前面的x为函数参数
# 不必担心函数名冲突；匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
def build(x, y):
    return lambda: x * x + y * y    #也可以作为返回值return

# 4.装饰器：为已经存在的对象/函数添加额外的功能，但不更改原对象/函数。@ 符号就是装饰器的语法糖
# 4.1记录函数执行日志，并不更改代码结构。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。
def use_logging(func):      #use_logging 就是一个装饰器，装饰本身的函数wrapper()

    def wrapper():      #通过foo调用需要使用参数，可以在wrapper中添加*args，表示多个参数，**kwargs表示多个关键字参数
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging    #加上这个可以省去foo = use_logging(foo)赋值
def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
# 4.2带参数的装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")      # 等价于@decorator
def foo(name='foo1'):
    print("i am %s" % name)

foo()
# 4.3类装饰器：装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点
# 使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()

# 存疑
# 4.4 functools.wraps：wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器里面的func函数中，使得装饰器里面的func函数也有和原函数foo一样的元信息
# 原本例子：
# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'with_logging'(并没有，而是f1)
        print (func.__doc__)      # 输出 None（并不是，而是does some math）
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f1(x):
   """does some math"""
   return x + x * x

#logged(f)
f1(1)
# 保留原函数元信息：
def logged1(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)     # 输出 'f2'
        print(func.__doc__)      # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged1
def f2(x):
   """does some math"""
   return x + x * x

f2(2)

def my_decorator(f):
     #@wraps(f)     #有没有都一样，存疑
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()

# 4.5 引用多个装饰器：相当于执行：f = a(b(c(f)))
#@a
#@b
#@c
def f ():
    pass

# 5.偏函数Partial function：通过设定参数的默认值，可以降低函数调用的难度
print(int('12345', base=8))     #字符串转为8进制int
print(int('12345', 16))     #16进制
#简化输入参数，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1000000', base=10))     #也可以设置其他参数

# 九、模块：在Python中，一个.py文件就称之为一个模块（Module）
# 1.1 任何模块代码的第一个字符串都被视为模块的文档注释
# 1.2 运行测试
hello.test()    # 执行hello模块里的test()
# 1.3作用域
# 类似__xxx__这样的变量是特殊变量，可以被直接引用
# 类似_xxx和__xxx这样的函数或变量就是非公开的，不应该被直接引用
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
# python搜索模块的路径
print(sys.path)

# 十、面向对象编程OOP：Object Oriented Programming：OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 1.类和实例
class Student(object):      #没有格式的继承类，就继承object类
    def __init__(self, name, score):    #创建__init__()方法，设置必须有的属性，第一个必定是self，调用时不用传递
        self.__name = name      #实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问，外部不能访问
        self.__score = score

    def print_score(self):      # 1.1 数据封装：在Student类的内部定义访问数据的函数，称为类的方法
        print('%s: %s' % (self.__name, self.__score))       #方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据

    def get_grade(self):        #可以直接增加新的方法
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    
    def set_score(self, score):     #添加方法允许外部设置score，并且可以做参数检查
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 59)    #创建实例
print(bart)
bart.print_score()      #调用方法
# 2.访问限制
bart.set_score(22)
# print(bart.score)       #私有name无法访问，输出name会报错
print(bart._Student__score)       #仍然可以通过_Student__name来访问__name变量，但强烈不建议
# 3.继承和多态
# 3.1继承：子类获得父类的全部功能
class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')     #当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()
class Cat(Animal):
    def run(self):
        print('Cat is running')

dog = Dog()
cat = Cat()
dog.run()
cat.run()
# 3.2多态：对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定
# 这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

run_twice(Tortoise())
# 3.3
# 对于静态语言（如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。只需要保证传入的对象有一个run()方法就可以了
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# 4.获取对象信息
# 4.1 type()判断对象是什么类型
print(type(abs))  
print(type(run_twice)==types.FunctionType)      #通过types模块的常量判断是否是一个函数
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
# 4.2 isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance(dog,Animal))
print(isinstance(123,int))      #也可以和type()一样判断基本类型
print(isinstance([1,2,3],(int,str)))        #判断是否是其中一种类型
print(isinstance((1, 2, 3), (list, tuple)))
# 4.3 获得一个对象的所有属性和方法，可以使用dir()函数，返回一个包含字符串的list
print(dir('ABC'))
# 配合getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态
print(getattr(bart,'_Student__name'))     #获取name属性
setattr(bart,'x',1)     #设置一个x属性，值为1
print(hasattr(bart,'x'))        #是否有属性x
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
# 在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
# 它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

# 5.实例属性和类属性
class test(object):
    name = 'test'       #类属性

t = test()
print(t.name)       #实例可以访问类属性
t.name = 'a'
print(t.name)       #相同名称的实例属性将屏蔽掉类属性，实例属性优先级高于类属性
print(test.name)        #类属性不会消失
del t.name      
print(t.name)       #删除实例属性后，便会输出类属性

# 十一、面向对象高级编程

# 1.使用__slots__
# 1.1 动态绑定允许我们在程序运行的过程中动态给class加上功能，即在class外部给类绑定方法
def set_name(self, name):
     self.name = name

Student.set_score = set_name
# 特殊的__slots__变量，可以限制该class实例能添加的属性
class Student1(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

amy = Student1()
# amy.score = 23        #会报错

# 1.2 __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent(Student1):
    pass

bob = GraduateStudent()
bob.score = 24      #不会报错

# 1.3使用@property：内置装饰器，负责把一个方法变成属性调用，将方法转换为相同名称的只读属性
class Student2(object):

    @property       # @property 装饰器会将 score() 方法转化为一个具有相同名称的只读属性的 "getter",        
    def score(self):        # 特征属性对象具有 getter, setter 以及 deleter 方法
        return self._score      # 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
        # 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
    @property
    def age(self):  # 只定义getter方法，不定义setter方法就是一个只读属性
        return 2021 - self._score

s = Student2()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
# s.score = 9999  # Error

# 1.4 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running')

class FlyableMixIn(object):
    def fly(self):
        print('Flying')

# 各种动物:
class Dog(Mammal,RunnableMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

class Parrot(Bird,FlyableMixIn):
    pass

class Ostrich(Bird,RunnableMixIn):
    pass

# 1.5定制类
# __str__()
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
class Student3(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):     # 定制print打印后的格式
         return 'Student object (name: %s)' % self.name
     __repr__ = __str__

print(Student3('Herry'))

# __iter__() 
# 如果一个类想被用于for  in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for i in Fib():
    print(i)

# __getitem__() 
# 像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib1()
print(f[5])     # f不能切片处理，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引，未对负数处理
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片，未对step参数处理
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f2 = Fib2()
print(f2[0:5])
# 对应的还有__setitem__()方法，把对象视作list或dict来对集合赋值。以及__delitem__()方法，用于删除某个元素。

# __getattr()__：动态调用，设置调用不存在的属性后的返回内容：值/函数
class Student4(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99.5
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s4 = Student4()
print(s4.score)
# print(s4.sex)     抛出异常错误

# __call__()：定义后可以直接对实例进行调用，完全可以把对象看成函数
class Student5(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student5('Herry')
s()     #可以直接输出My name is Herry
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(s))      #True

# 使用枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)    #value默认从1还是递增
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):        #从Enum派生自定义类
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#多种访问方式
print(Weekday.Wed)
print(Weekday(6))
print(Weekday['Tue'])

# 使用元类
# type()函数可以查看一个类型或变量的类型
print(type(Weekday))    #<class 'enum.EnumMeta'>
# 也可以动态创建出新的类
def fn(self, name='world'): # 先定义函数
     print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class，一次传入class名，继承类，class方法和函数绑定
h = Hello()
h.hello()

# metaclass:允许你创建类或者修改类.可以把类看成是metaclass创建出来的“实例”

# 给Mylist增加add方法：
class ListMetaclass(type):      # metaclass是类的模板，所以必须从`type`类型派生：
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass
# 使用场景：要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来

# 尝试编写ORM框架
# 1，编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User
# 其中父类Model和属性类型StringField、IntegerField由ORM框架提供，剩下的魔术方法比如save()全部由metaclass自动完成
'''
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
'''
# 2，首先来定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
# 进一步定义各种类型的Field，比如StringField，IntegerField
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')     #不懂

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')      #不懂

# 3,创建最复杂的ModelMetaclass：
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()       #不懂
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 4，创建基类Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

# 十二、错误、调试和测试

# 1。错误处理：
# 1.1 tryexceptfinally的错误处理机制
# 如果执行出错，则直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try')
    r = 10 / 0
    print('result:', r)
except ValueError as e:     # 可由多个except抛出多个错误
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:       # 如果没有错误发生，便会执行except后的else部分
    print('no error!')
finally:        # finally一定会被执行（也可以没有finally语句）
    print('finally')
print('END')
'''
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还捕获其子类
如下：
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:       这个错误不会被捕获，因为ValueError包含了UnicodeError
    print('UnicodeError')

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
# 可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally')

# 1.2 调用栈
#  出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

# 1.3 记录错误：内置的logging模块可以非常容易地记录错误信息
# 捕获错误可以让程序继续运行
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# 1.4抛出错误
# 可自定义错误class，建议使用内置的

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)       # raise语句手动抛出一个错误的实例
    return 10 / n

def bar():
    try:
        foo('1')
    except ValueError as e:
        print('ValueError!')
        raise       # 没有异常时默认引发 RuntimeError 异常；有异常时前面抛出过异常，这里就表示再引用一次

bar()

# 2。调试
# 2.1 断言assert
# 注意：断言的开关“-O”是英文大写字母O，不是数字0。可以python -O xx.py关闭assert，即assert相当于pass
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'     # 断言失败会抛出AssertionError
    return 10 / n

def main():
    foo('0')

# main()

# 2.2 logging：和assert比，logging不会抛出错误，而且可以输出到文件
# 允许指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

# 2.3 pdb:单步运行程序，python3 -m pdb xxx.py 
# 输入命令n可以单步执行代码；输入命令q结束调试，退出程序；输入命令l来查看代码
# 任何时候都可以输入命令p 变量名来查看已执行代码里的变量

# 2.4 pdb.set_trace():不需要单步执行，只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
s = '0'
n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停，可以用命令p查看变量，或者用命令c继续运行
# print(10 / n)

# 2.5 通过IDE设置断点

# 3。 单元测试：用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
# 见mydict.py mydict_test.py

# 4。文档测试doctest
# 以作为开始的内容就表示一行测试代码，并且接下来的一行则明确该测试代码的输出结果
def abs(n):
    '''
    Function to get absolute value of number.
    
    Example:
    
    abs(1)
    1
    abs(-1)
    1
    abs(0)
    0
    '''
    return n if n >= 0 else (-n)

if __name__=='__main__':
    doctest.testmod()       #什么输出都没有表示正常，没有问题

# 十三、IO编程
# IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。
# Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
# 对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。 
# 同步IO、异步IO：是否等待IO执行的结果。纯等待IO完成即同步，等的同时做别的事情即异步
# 使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂，比如重复询问是否完成，即轮询模式；操作方主动告知，即回调莫斯。
print('---------------------------------------------------------------------')
# 1。文件读写:读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，
# 通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# 1.1 读文件
try:
    file1 = open('/Users/herry/Documents/python/test.txt', 'r')
    print(file1.read())      # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
finally:
    if file1:
        file1.close()        #文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源。
        # 这里为了不管读取是否发生错误保证都会关闭使用tryfinally，但繁琐
# 引入with来自动调用close()方法：
with open('/Users/herry/Documents/python/test.txt', 'r') as file2:
    print(file2.read())
# 保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
# [1]如果文件很小，read()一次性读取最方便；
# [2]如果不能确定文件大小，反复调用read(size)比较保险；
# [3]如果是配置文件，调用readlines()最方便：
file3 = open('/Users/herry/Documents/python/test1.txt','r')
for line in file3.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

file4 = open('/Users/herry/Documents/附件1.png', 'rb')       #二进制文件使用rb模式读
print(file4.read())
file4.close()

file5 = open('/Users/herry/Documents/python/test1.txt', 'r', encoding='gbk', errors='ignore')     
#读取非utf-8编码encoding参数；errors表示如果遇到编码错误后如何处理，如文件中含有非法编码
print(file5.read())
file5.close()

# 1.2 file-like Object
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。

# 1.3 写文件:'w'删除重写 'a'追加
with open('/Users/herry/Documents/python/test1.txt', 'a') as file6:
    file6.write('zhui jia\n')

# 2.StringIO和BytesIO
# 2.1 StringIO:在内存中读写str
f4 = StringIO()
print(f4.tell())    # 0 stream position
f4.write('Hello ')
print(f4.tell())    # 6
f4.write('World!')
print(f4.tell())    # 12
print(f4.getvalue())    # getvalue()方法用于获得写入后的str

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
f5 = StringIO('Hello!\nHi!\nGoodbye!')
print(f5.tell())    # 0
'''
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
'''
print(f5.getvalue())


# 2.2 BytesIO:要操作二进制数据，就需要使用BytesIO
f6 = BytesIO()
f6.write('中国\n'.encode('utf-8'))
print(f6.getvalue())

# 3。操作文件和目录
print(os.name,'\n',os.uname(),'\n')
print(os.environ,'\n')       # 环境变量
print(os.environ.get('HOME'),'\n')

print(os.path.abspath('.'),'\n')     # 查看当前目录的绝对路径
print(os.path.join('.', 'testdir'))     # 查看要创建目录的合起来的路径，不同系统下斜杠不同
os.mkdir('./testdir')   # 创建新目录
os.rmdir('./testdir')   # 删除目录
# os.path.split()       拆分路径
print(os.path.splitext('/Users/herry/Documents/python/test1.txt')[1].strip('.'))     # 拆出文件类型    
# 列出当前目录所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录所有txt文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt'])

# 4.序列化：变量从内存中变成可存储或传输的过程称之为序列化
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
d1 = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d1))     # pickle.dumps()方法把任意对象序列化成一个bytes
# pickle.dump()直接把对象序列化后写入一个file-like Object
file7 = open('/Users/herry/Documents/python/test2.txt','wb')
pickle.dump(d1,file7)
file7.close()
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
'''
file8 = open('/Users/herry/Documents/python/test2.txt','wb')
d2 = pickle.load(file8)
file.close()
print(d2)
'''

# 4.1 JSON
# 要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，更好的是序列化为JSON。
# JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# 优点：JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取
j1 = json.dumps(d1)     #dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
print(d1)
print(j1)
# 反序列化json为python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = j1
print(json.loads(json_str)==d1)
# 序列化类的实例对象：
# 类的实例对象本身不是可序列化对象，可以编写转换函数转为dict类型
# 或者，通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量(少数例外，比如定义了__slots__的class)。
# 可以把任意class的实例变为dict：
s5 = Student5('herry')
print(s5)
print(json.dumps(s5, default=lambda obj: obj.__dict__))
# 反序列化为实例对象：
def dict2student(d):        
    return Student(d['name'], d['score'])

json_str = '{"score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))       #object_hook 一个可选函数，会被调用于每一个解码出的对象字面量（即一个 dict）。能够被用于实现自定义解码器

print(json.dumps({"c": 3, "b": 2, "a": 1}, sort_keys=True, indent=4))       #indent缩进，sort_keys以键值排序

# 十四、进程与线程
# 多任务的实现有3种方式：多进程模式；多线程模式；多进程+多线程模式(很少用)。
# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
# 多进程和多线程的程序涉及到同步、数据共享的问题

# 1.multiprocessing多进程

# 1.1 系统调用
# Unix/Linux操作系统提供了一个fork()系统调用，普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID
print('Process (%s) start' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

# 1.2 multiprocessing：multiprocessing模块提供了一个Process类来代表一个进程对象
'''
# 子进程要执行的代码。详见multi.py，这里运行会顺序错乱
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')
'''

# 1.3 Pool进程池：大量进程创建
'''
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)     # 默认是CPU核数，这里设置4表示最多同时可以跑4个子进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    p.close()
    p.join()
    print('All subprocesses done.')
'''

# 1.4 子进程：创建子进程后，通常子进程也是一个新的外部进程，还需要控制子进程的输入输出
# 示例，执行nslookup www.python.org
'''
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')    # communicate控制输入
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''
# 1.5 进程间通信：通过Queue、Pipes等多种方式来交换数据,详见queue-1.py
'''
def writeq(q):
    print("Process %s start to write" % os.getpid())
    for value in 'A' 'B' 'C':
        q.put(value)
    time.sleep(random.random())

def readq(q):
    print('Process %s start to read' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__' :
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=writeq, args=('q',))
    pr = Process(target=readq, args=('q',))
    # 启动子进程pw，开始写
    pw.start()
    # 启动子进程pr，开始读
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
'''

# 2.多线程:_thread是低级模块，threading是高级模块，对_thread进行了封装
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# 新线程执行的代码:
'''
这里运行会出现1 2 2 3 3 4 4 5 5 end end end end，正确详见loop.py
def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')    # 主线程实例的名字叫MainThread，子线程的名字在创建时指定
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''

# 2.1 Lock锁
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，线程的调度是由操作系统决定的
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量。示例如下：
# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        change_it(n)
'''
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)      # 每次结果都可能不一样，所以要给change_it()上一把锁，某个线程执行change时，其他线程不能执行
'''

'''
lock = threading.Lock()

def run_thread1(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。这里用tryfinally来确保锁一定会被释放。
            lock.release()

t3 = threading.Thread(target=run_thread1, args=(1,))
t4 = threading.Thread(target=run_thread1, args=(2,))
t3.start()
t4.start()
t3.join()
t4.join()
print(balance) 
'''
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
# 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

# 解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核

# 3. ThreadLocal
# 一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。解决了参数在一个线程中各个函数之间互相传递的问题。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 创建全局ThreadLocal对象:
'''
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t5 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t6 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t5.start()
t6.start()
t5.join()
t6.join()
'''

# 4. 进程和线程：

# 首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，
# 因此，多任务环境下，通常是一个Master，多个Worker。

# 多进程模式
# 优点：子进程挂掉不会影响其他进程
# 缺点：创建进程的代价大；操作系统能同时运行的进程数也是有限的

# 多线程模式：
# 优点：通常比多进程快一点
# 缺点：任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存

# IIS和Apache最初是多线程、多进程模式，现在是多进程+多线程混合模式

# 4.1 线程切换：操作系统在切换进程或者线程时需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），
# 然后把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。

# 4.2 计算密集型 vs. IO密集型

# 4.2.1 计算密集型：C
# 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。
# 这类任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，
# 所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
# 计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。
# 对于计算密集型任务，最好用C语言编写。

# 4.2.2 IO密集型：脚本语言Python
# 涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。
# 对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。
# IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

# 4.3 异步IO
# 如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型。
# Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务；在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
# 对于Python，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。

# 5.分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# 详见task-master.py task_worker.py

# 十五、正则表达式：匹配字符串
# 判断一个字符串是否是合法的Email的方法是：
# 1.创建一个匹配Email的正则表达式；2.用该正则表达式去匹配用户的输入来判断是否合法。

'''
规则：
\d     匹配一个数字
\w     匹配一个字母或数字
\s     匹配一个空格
.      匹配任意字符
*      匹配任意字符（包括0个）
+      匹配至少一个字符
?      匹配0个或1个字符
{n}    匹配n个字符
{n,m}  匹配n～m个字符
'''
# \d{3,4}\-\d{3,8}  可以匹配带区号的电话号码，如010-12345678
'''
进阶：[]更精确，表示范围
[0-9a-zA-Z\_]    匹配一个数字、字母或者下划线
[0-9a-zA-Z\_]+   匹配至少由一个数字、字母或者下划线组成的字符串
[a-zA-Z\_][0-9a-zA-Z\_]*    匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，即Python合法变量名
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}  更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
A|B     匹配A或者B，如(P|p)ython可以匹配Python和python
^   表示行开头，如^\d 表示必须一个数字开头
$   表示行结尾，如\d$ 表示必须一个数字结尾
'''
# Python使用re模块提供正则表达式匹配操作
re.match(r'^\d{3,4}-\d{3,8}$','010-12345678')       # 如果匹配成功，返回一个Match对象，否则返回None
# 常见用法如下
test_str = '010-12345678'
if re.match(r'^\d{3,4}-\d{3,8}$',test_str):     # 加上r，可以不用转义
    print('ok')
else:
    print('error')

# 1.切分字符串
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 2.分组()
m1 = re.match(r'^(\d{3,4})-(\d{3,8})$', '010-12345678')
print(m1.group(0))     # group(0)永远是原始字符串
print(m1.group(1))
print(m1.group(2))

m2 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', '17:17:22')
print(m2.groups())      # 返回一个元组，包含所有匹配的子组

# 3.贪婪匹配：尽可能匹配最多的字符串，正则表达式默认是贪婪匹配
# 加个?就可以让\d+采用非贪婪匹配，否则第一个会把后面的0都匹配到，使得第二个元素是空
m3 = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(m3)

# 4.编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；2.用编译后的正则表达式去匹配字符串。
# 如果一个正则表达式要重复使用多次，可以预编译该正则表达式，后续使用可以不再编译，直接匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串

# 练习：
# 判断是否有效邮箱地址：
def is_valid_email(addr):
    a = re.compile(r'^[\w.]+@[0-9a-zA-Z]+.[a-zA-Z]+$')
    if a.match(addr):
       return True

# 提取邮箱地址中的名字
def name_of_email(addr):
    new = re.split(r'@',addr)[0]
    b = re.compile(r'<(\w+\s\w+)>|(\w+)')
    a= b.match(new)
    #print(a[0],'',a[1])
    if a[1]:
         return a[1]
    else:
         return a[0]

print((name_of_email('<Tom Paris> tom@voyager.org')=='Tom Paris') & (name_of_email('tom@voyager.org') == 'tom'))


# 十六、常用内建模块

# 1.datetime：处理日期和时间的标准库
print(datetime.now())      # 如果仅导入import datetime，则必须引用全名datetime.datetime，第一个模块，第二个类
dt = datetime(2022, 4, 19, 12, 20)      # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())   # 把datetime转换为timestamp，python的timestamp是一个浮点数
# 如Java和JavaScript等其他的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
t = 1429417200.0
print(datetime.fromtimestamp(t))    # 从timestamp转为datetime
print(datetime.utcfromtimestamp(t)) # UTC时间
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))  # str转datetime，结果无时区信息
print(datetime.now().strftime('%a, %b %d %H:%M'))     #datetime转str
print(datetime.now()+timedelta(days=1,hours=1))     #datetime加减
# 本地时间转utc时间，本地现在是utc+8，utc是utc+0：datetime类型有一个时区属性tzinfo，默认为None
tz_utc_8 = timezone(timedelta(hours=8))     #创建时区utc+8:00
dt1 = datetime.now().replace(tzinfo=tz_utc_8)    # 强制设置为UTC+8:00
print(dt1)
# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=-8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

# 练习：获取了日期和时间如2015-1-21 9:01:30，时区信息如UTC+5:00，均是str，将其转换为timestamp
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    num = int(re.match(r'UTC([+-]\d+):',tz_str).group(1))
    ts = dt.replace(tzinfo=timezone(timedelta(hours=num)))
    return ts.timestamp()

# 2.collections:提供集合类
# 2.1 namedtuple：命名元组  具备tuple的不变性，又可以根据属性来引用
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0]+p[1])
x,y=p
print(x,y)
print(p.x,p.y)      # 可以用属性而不是索引来引用tuple的某个元素
Circle = namedtuple('Circle', ['x', 'y', 'r'])  #定义一个圆

# 2.2 deque:高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['x','y','z'])
q.append('1')
q.appendleft('0')   # 相对应的也有popleft
print(q)

# 2.3 defaultdict：key不存在时，可以返回一个默认值而不是报错，其他和dict一致
dd = defaultdict(lambda:'N/A')
print(dd[key])      # # key不存在，返回默认值N/A

# 2.4 OrderedDict:保持dict的key顺序
d2 = dict([('a', 1), ('b', 2), ('c', 3),('d',4)])
print('dict:',d2)
d3 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])    
print('OrderedDict:',d3)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序，可以实现一个FIFO先进先出的dict,当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# 2.5 ChainMap:把一组dict串起来并组成一个逻辑上的dict
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))

# 适用场景：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
# 如下，查找user和color参数
# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }
'''
./test.py -u herry -c blue 命令行参数的优先级较高
'''


# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 2.6 Counter:计数器，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
c.update('herry')
print(c)

# 3.base64：用64个字符来表示任意二进制数据
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

# 练习：能处理去掉=的base64解码函数
def safe_base64_decode(s):
    l = (len(s)*6)%8
    if l==0:
       return base64.b64decode(s)
    else:
       s = s + '='*l
       return base64.b64decode(s)

assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

# 4.struct:解决bytes和其他二进制数据类型的转换,bytes:b'str'
# pack把其他数据类型转为bytes，unpack把bytes转为其他
print(struct.pack('>I',10240099))   # >I 处理指令：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))    # H:2字节无符号整数

# 分析bmp位图文件
# 假设s为位图前30个字节
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# 通常，两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0； 
# 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度；
#  一个2字节整数：始终为1； 一个2字节整数：颜色数。
print(struct.unpack('<ccIIIIIIHH', s))      # 读取s文件头其中的参数，BMP格式采用小端方式存储数据

# 练习：检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    result = struct.unpack('<ccIIIIIIHH',data[:30])
    if (result[0]==b'B') & ((result[1]==b'M') | (result[1]==b'A')):     # if inf_t[0:2] in [(b'B',b'M'),(b'B',b'A')]:
       width=result[6]
       height=result[7]
       color=result[9]
    return {
        'width': width,
        'height': height,
        'color': color
    }
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

# 5.hashlib:提供常见的摘要（哈希/散列）算法
# 适用于存储登录用户名和口令的摘要到数据库
md5 = hashlib.md5()     # md5改为sha1也是一样的
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))     #如果数据量很大，可以分块多次调用update(),结果一样
print(md5.hexdigest())

sha256 = hashlib.sha256()
sha256.update('Hello World'.encode('utf-8'))
print(sha256.hexdigest())
# 加盐hash：防止黑客通过彩虹表根据哈希值反推原始口令，确保存储的用户口令不是那些已经被计算出来的常用口令的MD5
# 如果假定用户无法修改登录名，就可以通过把一部分随机数作为Salt和用户名合起来计算MD5，从而实现相同口令的用户也存储不同的MD5。
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

# 6.hmac：Keyed-Hashing for Message Authentication算法。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
# 使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
# 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
# 如上一个练习可以更改为：
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

def login_1(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 7.itertools：提供用于操作迭代对象的函数
'''
natuals = itertools.count(1)    # count()会创建一个无限的迭代器,只能按Ctrl+C退出
for n in natuals:
    while n<10:     #即使添加while循环条件也并没有停止
        print(n)
        n+=1

cs = itertools.cycle('ABC') # 注意字符串也是序列的一种,cycle()会把传入的一个序列无限重复下去,同样职能Ctrl+C退出
for c in cs:
    print(c)
'''
ns = itertools.repeat('A', 3)   #repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
for n in ns:
    print(n)
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)    # takewhile()等函数根据条件判断来截取出一个有限的序列
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):     # chain()把一组迭代对象串联起来，形成一个更大的迭代器
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):     # groupby()把迭代器中相邻的重复元素挑出来放在一起
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):    # 将a识别为A和A放在一起
    print(key, list(group))

# 练习：计算Pi(N)
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, 
    one = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, , 2*N-1.
    two = list(itertools.takewhile(lambda x:x<=2*N-1,one))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, 
    three = [4/i if two.index(i) % 2 == 0 else -4 / i for i in two]
    # step 4: 求和:
    return sum(three)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

# 8.contextlib：简化上下文管理器写法
# 通常一个类只要实现了__enter__()和__exit__()，我们就称之为上下文管理器。with语句的expression是上下文管理器，
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s' % self.name)

with Query('Bob') as q:     # as后的变量即__enter()__返回的变量，Query('Bob')即expression，上下文管理器
    q.query()

# 但这种写两个方法的也比较繁琐，contextlib模块包含一个装饰器contextmanager和一些辅助函数，装饰器contextmanager只需要写一个生成器函数就可以代替自定义的上下文管理器
class Query1(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query1(name)
    yield q
    print('End')

# 在代码执行前后实现上下文管理,代码的执行顺序是：
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>。
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# 1.1 @closing
# 如果一个对象没有实现上下文，就不能把它用于with语句。但可以用closing()来把该对象变为上下文对象。
'''
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
'''
# closing也是一个经过@contextmanager装饰的generator
'''
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''

# 9.urllib:提供一系列用于操作URL的功能
# 1.Get:
# 如对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650 进行抓取，并返回响应
with request.urlopen('https://www.google.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    #print('Data:', data.decode('utf-8'))

# 添加request头模仿浏览器请求
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

# 2.Post：发送一个请求，只需要把参数data以bytes形式传入
# 模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
'''
print('Login to weibo.cn')
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

# 3.Handler:通过一个Proxy去访问网站
print('----------------------------------------')
'''
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
'''

# 10.XML
# 操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。通常我们关心的事件是start_element，end_element和char_data
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。
# 内容多建议使用json

# 11.HTMLParser：解析HTML页面
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>       
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial<br>END</p>
</body></html>''')      # feed可以多次调用

# 练习详见lianxi.py
