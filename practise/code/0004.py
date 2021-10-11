#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re,string
from collections import Counter

with open('/Users/herry/Documents/python/text.txt','r') as text:
    data1 = text.read().replace('\n',' ').replace('\r',' ')
    # 去除英文标点，string.punctuation包含所有英文符号
    for i in string.punctuation:
        data1 = data1.replace(i,'')
    data1 = data1.split(' ')
    a = re.compile(r'\w+')
    data2 = map(a.findall,data1)
    result = list(data2)
    print('该文本一共有 %s 个单词，分别如下' % len(result))
    c = [str(j) for j in result]
    b = Counter(c).most_common()
    print(b)
