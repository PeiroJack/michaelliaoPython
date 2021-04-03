#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Sql_forengin import Student, StudyRecord

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test?charset=utf8', encoding="utf-8")
Session_class = sessionmaker(bind=engine)
session = Session_class()

# stu_obj = session.query(StudyRecord).filter_by(id= 100).first()
# stu_obj = session.query(StudyRecord.id, StudyRecord.day).all()
'''
stu_obj = session.query(StudyRecord).all()
for i in range(3):
    print(stu_obj[i].student.id)
    print(stu_obj[i].student.name)
    print(stu_obj[i].student.register_day)
'''

'''
stu_obj = session.query(StudyRecord).filter_by(day = 90).all()

print(stu_obj[0].student.id)
print(stu_obj[0].student.name)
print(stu_obj[0].student.register_day)
'''

stu_obj = session.query(StudyRecord).filter_by(day = 3).one()

print(stu_obj.student.id)
print(stu_obj.student.name)
print(stu_obj.student.register_day)

print(stu_obj)
print(type(stu_obj))

'''
返回值          结果
All()           列表
First()         一个对象
One()           一个对象