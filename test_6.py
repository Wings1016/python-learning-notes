#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
import sqlite3
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 二十二、访问数据库
# MySQL，大家都在用，一般错不了；PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；sqlite，嵌入式数据库，适合桌面和移动应用。

# 1.mysql:pip install mysql-connector-python
conn = mysql.connector.connect(user='root',password='Trust123!',database='python_test')
# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Herry'])
print(cursor.rowcount)
# 提交事务:
conn.commit()       # 执行INSERT等操作后要调用commit()提交事务；MySQL的SQL占位符是%s。
# 查询
# 使用Cursor对象执行select语句时，通过fetchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()
print('value:%s' % values)

# 关闭Cursor和Connection:
cursor.close()
# 关闭数据库连接
conn.close()


# 2.sqlite:嵌入式数据库，体积很小，python有内置
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn1 = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor1 = conn1.cursor()
# 执行一条SQL语句，创建user表:
cursor1.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor1.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
print(cursor1.rowcount)
# 执行查询语句,占位符是？:
cursor1.execute('select * from user where id=?', ('1',))
# 获得查询结果集:
values1 = cursor1.fetchall()
print(values1)
# 关闭Cursor:
cursor1.close()
# 提交事务:
conn1.commit()
# 关闭Connection:
conn1.close()

