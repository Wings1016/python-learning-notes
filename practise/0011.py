#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#敏感词文本文件 filtered_words.txt，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

with open('//Users/herry/Documents/python/practise/filter_words.txt') as f:
    words = [i.strip('\n') for i in f.readlines()]

a = input('请输入：')
b = False

if a:
    for word in words:
        if a == word:
            b = True
            print('Freedom')
            break

if b == False:
    print('Human Rights')

# print(list(a).sort())
