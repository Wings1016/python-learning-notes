#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 敏感词文本文件 filtered_words.txt，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

with open('//Users/herry/Documents/python/practise/filter_words.txt') as f:
    words = [i.strip('\n') for i in f.readlines()]

a = input('请输入：')
b = False
c = list(a)

if a:
    for word in words:
        if word in a:
            b = True
            index = a.find(word)
            for i in range(len(word)):
                c[i+index]='*'
            result = ''.join(c)
    
if b:    
    print(result)
else:
    print(a)