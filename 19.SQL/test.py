#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('C:\\Users\\peiroJack\\Desktop\\michaelliao\\Python\\19.SQL')

from models import User,Solary
from sql_insert import insert
from sql_select import selest
from sql_create import create_table

create_table(Solary)

new_user = User(id='8', name='miko')

insert(new_user)
print('产生新的用户')

data = selest(User)

for i in data:
    print(i.id, i.name)