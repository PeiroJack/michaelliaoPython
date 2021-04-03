#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey  #导入外键
from sqlalchemy.orm import  relationship  #创建关系
  
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
 
Base = declarative_base() #生成orm基类

class Company(Base):

    __tablename__ = "company"

    name = Column(String(20),primary_key=True)
    location = Column(String(20))
  
    def __repr__(self):
        return "name:{0} location:{1}".format(self.name,self.location)
  
class Phone(Base):
     
    __tablename__ = "phone"

    id = Column(Integer,primary_key=True)
    model = Column(String(32))
    price = Column(String(32))
    # company是主表，phone是从表。
    # 查询phone表，返回phone_obj，可以通过phoen_obj.Company查询到company中外键关联的数据。
    # 查phone表返回company表里的数据。这个称之为：正向查询。
    company_name = Column(String(32),ForeignKey("company.name"))
    # company是主表，phone是从表。
    # 查询company表，返回company_obj，可以通过company_obj.phone_of_company查询到phone表的外键关联数据。
    # 查company表返回phone表里的数据。这个称之为：反向查询。
    company = relationship("Company",backref="phone_of_company") 
  
    def __repr__(self):
        return "{0} model:{1},sales:{2} price:{3}".format(self.id,self.model,self.sales,self.price)
  
Base.metadata.create_all(engine) #创建表