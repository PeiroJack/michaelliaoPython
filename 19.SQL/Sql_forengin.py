#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey  #导入外键
from sqlalchemy.orm import  relationship  #创建关系

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/test?charset=utf8', encoding="utf-8")

Base = declarative_base() # 生成orm基类

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=True)
    register_day = Column(DATE, nullable=False)

    #def __repr__(self):
    #    return '<{0} name:{1}>'.format(self.id, self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))
    student = relationship('Student', backref='my_study_record')

    #def __repr__(self):
    #    return '<{0} name:{1} day:{2} stu_id:{3}>'.format(self.id, self.student.name, self.day, self.stu_id)

if __name__ == '__main__':
    Base.metadata.create_all(engine) # 创建表