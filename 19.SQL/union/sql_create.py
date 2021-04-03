#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, MetaData, ForeignKey, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

meta = MetaData()

# 定义User对象
class Student(Base):
    __tablename__ = 'student'
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

class Family(Base):
    __tablename__ = 'family'
    id = Column(String(20), primary_key=True)
    member = Column(Integer)
    student_id = Column(String(20), ForeignKey('student.id'))

class House(Base):
    __tablename__ = 'house'
    id = Column(String(20), primary_key=True)
    location = Column(String(100))
    family_id = Column(String(20), ForeignKey('family.id'))

class Car(Base):
    __tablename__ = 'car'
    id = Column(String(20), primary_key=True)
    name = Column(String(100))
    family_id = Column(String(20))

def create_fun():
    # 初始数据库连接：
    engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/mydb?charset=utf8', echo=True)
    # 创建DBSession
    DBSession = sessionmaker(bind=engine)

    # 创建session会话，数据库操作的基石
    session = DBSession()

    # 在数据库中创建表user
    Student.metadata.create_all(bind=engine)
    Family.metadata.create_all(bind=engine)
    House.metadata.create_all(bind=engine)
    Car.metadata.create_all(bind=engine)

    #插入数据
    stu_one = Student(id='1', name = '悟空')
    stu_two = Student(id='2', name = '贝吉塔')
    stu_three = Student(id='3', name = '比克')
    stu_four = Student(id='4', name = None)

    # 提交数据到session

    session.add(stu_one)
    session.add(stu_two)
    session.add(stu_three)
    session.add(stu_four)

    session.commit()

    family_one = Family(id='1',member=7,student_id='1')
    family_two = Family(id='2',member=5,student_id='2')
    family_three = Family(id='3',member=8,student_id='3')

    session.add(family_one)
    session.add(family_two)
    session.add(family_three)
    session.commit()

    house_one = House(id='1',location='地球',family_id='1')
    house_two = House(id='2',location='贝吉塔星',family_id='2')
    house_three = House(id='3',location='美克星人',family_id='3')
    house_four = House(id='4',location='地球',family_id='3')

    session.add(house_one)
    session.add(house_two)
    session.add(house_three)
    session.add(house_four)

    session.commit()

    car_one = Car(id='1',name='筋斗云',family_id='1')
    car_two = Car(id='2',name='奔驰',family_id='2')
    car_three = Car(id='3',name='宝马',family_id='3')

    session.add(car_one)
    session.add(car_two)
    session.add(car_three)

    #提交到数据库
    session.commit()

    session.close()

if __name__ == '__main__':
    create_fun()