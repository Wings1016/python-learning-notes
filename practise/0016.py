#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中
'''

import json
from openpyxl import Workbook

with open('./numbers.txt') as f:
    data = json.load(f)     # [[1, 82, 65535], [20, 90, 13], [26, 809, 1024]]

wb = Workbook()
dest_filename = 'numbers.xlsx'
ws1 = wb.active
for row in range(1, len(data)+1):
    for col in range(1, len(data[0])+1):
        _ = ws1.cell(column=col, row=row, value=data[row-1][col-1])
wb.save(filename=dest_filename)
