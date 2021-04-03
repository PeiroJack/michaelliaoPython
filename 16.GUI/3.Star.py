#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import *

def drawStar(x, y):
    pu() # penup 起笔
    goto(x, y) # 去到
    pd() # 落笔
    # set heading: 0
    seth(0) # setheading
    for i in range(5):
        fd(40) # 前进
        rt(144) # 右转

# range(0, 250, 50) 0-250 每50一间隔
for x in range(0, 250, 50):
    drawStar(x, 0)

done()