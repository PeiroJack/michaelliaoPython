#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, sqlite3
# os.path.dirname(__file__) 获得当前文件目录路径
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):

    conn1 = sqlite3.connect(db_file)
    cursor = conn1.cursor()
    cursor.execute("select name from user where score >= ? and score <= ?  order by score asc;",(low,high))
    values = cursor.fetchall()
    result = []
    for v in values:
        result.append(v[0])#values返回的是一个列表，但是里面元素是一个tuple,需要转换成list,元素是个字符窜型
    cursor.close()
    conn1.close()
    return result

    
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')