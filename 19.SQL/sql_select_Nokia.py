#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine
from sql_foreign_models import Company, Phone

engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/test",)
Session_class = sessionmaker(bind=engine)
session = Session_class()

#查询company表
company_obj = session.query(Company).filter_by(name = "Nokia").first()

#通过phone表关联的relationship的字段"backref="phone_of_company"",查询phone表数据
print(company_obj.phone_of_company[0].id)
print(company_obj.phone_of_company[0].model)
print(company_obj.phone_of_company[0].price)
print(company_obj.phone_of_company[0].company_name)