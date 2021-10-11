#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一个HTML文件，找出里面的正文;找出里面的链接。

from bs4 import BeautifulSoup
# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库

result = []
i = 0
with open('./sina.html') as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.body.text)    #正文，或者用soup.gettext()
    for link in soup.findAll('a'):
        pass
        #print(link.get('href'))     # 链接
    img = soup.find_all('img')
    for i in range(len(img)):
        result.append(img[i].attrs['src'])
    print(result)