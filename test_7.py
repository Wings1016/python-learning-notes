#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 3.最有名的ORM框架是SQLAlchemy
'''
[
    ('1', 'Michael'),
    ('2', 'Bob'),
    ('3', 'Adam')
]
用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
即ORM：Oriented-Related-Mapping，把关系数据库的表结构映射到对象上
anaconda中包含sqlalchemy
'''
# 创建基类
Base = declarative_base()

class User(Base):       # 如果还有其他表，创建另外class
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接create_engine():'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:Trust123!@localhost:3306/python_test')
# 创建DBsession类型
DBSession = sessionmaker(bind=engine)

# 有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象,DBSession对象可视为当前数据库连接
session = DBSession()
# 创建新user对象
new_user = User(id='',name='Jake')
# 添加到session
# session.add(new_user)
# 提交保存到数据库
# session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
print('books:', user.books[0].name)
# 关闭session
session.close()

'''
例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
'''