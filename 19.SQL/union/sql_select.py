#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,and_,or_
from sql_create import Student,Family,House,Car
 
# print "初始化数据库引擎"
engine = create_engine("mysql+mysqldb://root:123456@localhost:3306/mydb?charset=utf8")
 
# print "创建session对象"
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
 
 
def select_join():
    ''' 
    result = session.query(Student)
    print('sql语句：')
    print(result)
 
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print (x.id,x.name)
    '''
    
    '''
    result = session.query(Family)

    print ('sql语句：')
    print(result)
 
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print (x.id,x.member)
    '''

    '''
    result = session.query(House)
    print ('sql语句：')
    print(result)
 
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print (x.id,x.location)
    '''
 
    '''
    result = session.query(Car)
    print ('sql语句：')
    print(result)
 
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print (x.id,x.name)
    '''

    '''
    print('两张表联表查询')
    print('Student表joinFamily表，通过查找Family表中member字段大于6的Student表中数据')
    result = session.query(Student).join(Family).filter(Family.member>6)
    
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''
 
    '''
    #三张表连表查询
    result = session.query(Student).join(Family).join(House).filter(House.location=='美克星人')
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''
    
    '''
    #没有外键关系的join查询。car与其他表没有外键关系
    result_three = session.query(Student).join(Family).join(Car).filter(Car.name=='宝马')
    # sqlalchemy.exc.InvalidRequestError: Don't know how to join to <class 'sql_create.Car'>.
    print('result的数据类型:')
    print(type(result_three))
 
    print('查询结果:')
    for x in result_three:
        print(x.id, x.name)
    '''
    
    '''
    #在没有外键关联的情况下使用join连接两张表
    result = session.query(Student).join(Family).join(Car,Car.family_id==Family.id).filter(Car.name=='宝马')
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''
 
    '''
    #or 操作
    result = session.query(Student.name,Family.member,House.location).join(Family).join(House).filter(or_(House.location=='地球',Family.member==7))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.name, x.member, x.location)
    '''

    '''
    #in操作
    result = session.query(Student.name,Family.member).join(Family).filter(Family.member.in_((4,5,6)))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.name, x.member)
    '''

    '''
    #offset
    result = session.query(Student).offset(2)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''

    '''
    #limit
    result = session.query(Student).limit(2)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''

    '''
    #~取反操作
    result = session.query(Student.name,Family.member).join(Family).filter(~Family.member.in_((4,5,6)))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.name, x.member) 
    '''

    '''
    #between
    result = session.query(Student).filter(Student.id.between(1,2))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name) 
    '''
    
    '''
    #like
    result = session.query(Student).filter(Student.name.like('悟%'))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name) 
    '''

    '''
    result = session.query(Student).filter(Student.name.like('悟'))
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name) 
    '''

    '''
    #空值判断
    result = session.query(Student).filter(Student.name.is_(None))
    print(result)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''
     
    '''
    result = session.query(Student)
    print(result)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)
    '''

    '''
    result = session.query(Student).all()
    print(result)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x.id, x.name)

    '''

    '''
    result = session.query(Student).filter(Student.id=='1')
    print(result)
    print('result的数据类型:')
    print(type(result))
 
    print('查询结果:')
    for x in result:
        print(x)
        print(x.id, x.name)
    '''
    



if __name__ == "__main__":
    select_join() 
    # print '关闭数据库连接'
    session.close()