#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 在Python中，最有名的ORM框架是SQLAlchemy。

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


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
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# DBSession对象可视为当前数据库连接。

# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()