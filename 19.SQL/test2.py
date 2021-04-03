#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sql_foreign_models import Company
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test')

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 默认的外键关联的动作是  “.set null”，即主表删除数据，附表中关联的字段设为空。
company = session.query(Company).filter_by(name="Sungsum").first()
session.delete(company)
session.commit()