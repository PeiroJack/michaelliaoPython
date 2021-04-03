#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('C:\\Users\\peiroJack\\Desktop\\michaelliao\\Python\\19.SQL')

from sqlalchemy import create_engine
from models import User

# DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='123456', server='localhost:3306', database='test')

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# engine = create_engine(DATABSE_URI)
def create_table(table_name):
    table_name.metadata.create_all(engine)
    print('创建成功')