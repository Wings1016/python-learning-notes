#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random,string
import mysql.connector

# 连接mysql数据库

conn = mysql.connector.connect(user='root',password='Trust123!',database='python_test')
cursor = conn.cursor()
# 生成激活码并插入到表中
i = 0   # 计数器
while(i<200):
    ran_code = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    cursor.execute('INSERT INTO code(code) values(\'%s\')' % (ran_code))
    conn.commit()      # 执行INSERT等操作后要调用commit()提交事务；
    # mysql会自动给%s添加引号，所以要去掉ran_code字符串的引号，否则会报1064错误
    i+=1

# 关闭Cursor和Connection:
cursor.close()
# 关闭数据库连接
conn.close()