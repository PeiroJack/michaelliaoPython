#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sql_foreign_models import Phone, Company

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test',)
Sesison_class = sessionmaker(bind=engine)
session = Sesison_class()

# 查询phone表
phone_obj = session.query(Phone).filter_by(id = 1).first()
# 通过phone表关联的relationship字段"Company"查询出company表的数据
print(phone_obj.company.name)
print(phone_obj.company.location)