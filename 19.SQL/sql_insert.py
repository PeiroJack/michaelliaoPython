#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('C:\\Users\\peiroJack\\Desktop\\michaelliao\\Python\\19.SQL')


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import User

def insert(new_data):
    #DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='123456', server='localhost:3306', database='test')
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
    #engine = create_engine(DATABSE_URI)
    print('创建数据库引擎')

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print('创建session对象')

    session.add(new_data)
    print('添加数据到session')

    session.commit()
    print('提交数据到数据库')

    session.close()
    print('关闭数据库连接')

if __name__ == '__main__':
    insert(User)