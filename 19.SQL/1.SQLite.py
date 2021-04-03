#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect(r'19.SQL\test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')
# 通过rowcount获得插入的行数:
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
cursor.rowcount
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 试试查询记录
conn = sqlite3.connect(r'19.SQL\test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集:
# 使用Cursor对象执行select语句时，通过fetchall()可以拿到结果集。
# 结果集是一个list，每个元素都是一个tuple，对应一行记录。
values = cursor.fetchall()
values
cursor.close()
conn.close()