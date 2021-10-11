#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中
'''

import re
from openpyxl import Workbook

# 获取txt有效数据
data1 = list()
with open('./students.txt') as f:
    data = [i.strip('\t\n') for i in f.readlines()]
    for i in range(len(data)-2):
        data1.append(data[i+1])
    print(data1[0])

# 匹配

def pp(data2):
    pattern = re.compile(r'^"(\d+)":\["(\w+)",(\d{2,3}),(\d{2,3}),(\d{2,3})\]')
    result = pattern.match(data2).groups()
    return result

# 字符串内容是数字转数字，否则存入excel会有警告

def str2num(data3):
    if data3.isdigit():
        return eval(data3)
    else:
        return data3


wb = Workbook()
dest_filename = 'student.xlsx'
ws1 = wb.active
for row in range(1, len(data1)):
    for col in range(1, 6):
        _ = ws1.cell(column=col, row=row,
                     value=str2num(pp(data1[row-1])[col-1]))
wb.save(filename=dest_filename)
