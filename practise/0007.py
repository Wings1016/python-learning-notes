#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os,re
from itertools import (takewhile, repeat)

'''
def iter_count(file_name):
    buffer = 1024 * 1024
    with open(file_name) as f:
        # takewhile：创建一个迭代器，只要 predicate 为真就从可迭代对象中返回元素
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)
'''

def cal_comment(data):
    pattern = re.compile(r'[\s]*#')
    return filter(pattern.match,data)

'''
测试正则表达式pattern
with open('./code/0006.py') as f:
    data = f.readlines()
    print(list(cal_comment(data)))
'''

for roots,dirs,name in os.walk('/Users/herry/Documents/python/practise/code/'):
    for file_ in name:
        with open('/Users/herry/Documents/python/practise/code/%s' % file_) as f:
            data = f.readlines()
            all_ = len(data)
            kong = len(list(filter(lambda x:x=='\n',data)))
            comment = len(list(cal_comment(data)))
            print(file_,':共',all_,'行；其中注释行数：',comment,'；空行数：',kong)

