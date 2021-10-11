#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os,string,re
from collections import Counter

# 处理英文文本转为list
def deal(txt):
    data1 = txt.read().replace('\n',' ').replace('\r',' ')
    # 去除英文标点，string.punctuation包含所有英文符号
    for i in string.punctuation:
        data1 = data1.replace(i,'')
    data1 = data1.split(' ')
    a = re.compile(r'\w+')
    data2 = map(a.findall,data1)
    return list(data2) 

for root, dirs, name in os.walk('./diary/'):
    for txtfile in name:
        with open('./diary/%s' % txtfile) as txt:
            result = deal(txt)
            c = [str(j) for j in result]
            b = Counter(c).most_common(1)
            print(txtfile,':',b)