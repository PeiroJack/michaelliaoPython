#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('C:\\Users\\peiroJack\\Desktop\\michaelliao\\Python\\19.SQL')


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Solary

def selest(table_name):
    #DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='123456', server='localhost:3306', database='test')

    engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test')
    #engine = create_engine(DATABSE_URI)
    print('初始化数据库引擎')

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    print('创建session对象')

    table_data = session.query(table_name).all()
    print('查询')

    session.close()

    return table_data

if __name__ == '__main__':
    selest_fun(User)



