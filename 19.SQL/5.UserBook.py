#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  relationship  #创建关系

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
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

# 初始化数据库连接:
# create_engine()用来初始化数据库连接。
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
#engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象:
session = DBSession()
# 创建新Book对象：
new_book = Book
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
