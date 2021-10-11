#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
from itertools import (takewhile, repeat)

def iter_count(file_name):
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)

for roots,dirs,name in os.walk('/Users/herry/Documents/python/practise/code/'):
    for file_ in name:
        iter_count(file_)