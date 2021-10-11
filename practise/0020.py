#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
根据通话详单.xls 文件。写代码，对每月通话时间做个统计。
'''

import re
import xlrd

# 读取xls数据，并存储到date，time
wb = xlrd.open_workbook('./2021年02-04月语音通信.xls')
sh = wb.sheet_by_index(0)

date,time = [],[]
for rx in range(sh.nrows):
    date.append(sh.row(rx)[2].value)
    time.append(sh.row(rx)[3].value)

# 按月份存储结果
feb = [date[i] for i in range(len(date)) if re.match('^2021-02',date[i])!=None]
mar = [date[i] for i in range(len(date)) if re.match('^2021-03',date[i])!=None]
apr = [date[i] for i in range(len(date)) if re.match('^2021-04',date[i])!=None]
result = [feb,mar,apr]
summ = [[0,0],[0,0],[0,0]]

# 转为标准时间
def convert_time(minutes,seconds):
    all = minutes*60+seconds
    h = all//3600
    m = (all%3600)//60
    s = all%3600%60
    st = '%s:%s:%s' % (h,m,s)
    return st

# 匹配分秒，提取数字
def convert2num(time):
    # wao = re.compile('^(?:([0-9]+)?分)?(?:([0-9]+)秒)?')
    min = re.search('^(\d+)分',time)
    sec = re.search('(\d+)秒$',time)
    if min==None:
        min=0
    else:
        min = eval(min.group(1))
    return [min,eval(sec.group(1))]
    
time = [convert2num(time[i+1]) for i in range(len(time)-1)]
time = [time[0:len(feb)],time[len(feb):len(feb)+len(mar)],time[len(feb)+len(mar):]]   #划分三部分

# 分秒求和
for i in range(len(result)):
    for j in range(len(result[i])):
        summ[i][0]+=time[i][j][0]
        summ[i][1]+=time[i][j][1]

for i in range(len(summ)):
    final = convert_time(summ[i][0],summ[i][1])
    print('第%s月总通话时间为：%s' % (i+2,final))